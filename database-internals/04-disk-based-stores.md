### Detailed Notes of Chapter 4: Disk-Based Stores from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter explores the architecture and mechanics behind disk-based storage systems in databases.
- Disk-based stores are essential for persisting large volumes of data that cannot fit entirely in memory.

### Key Concepts

1. **Disk-Based Storage Fundamentals:**
   - **Definition:** Storage systems that rely on disk drives (HDDs or SSDs) to persist data.
   - **Purpose:** To handle large datasets and ensure data durability and persistence across system restarts and failures.

2. **Storage Media:**
   - **HDDs (Hard Disk Drives):**
     - Magnetic storage media with spinning disks.
     - High capacity but slower random access compared to SSDs.
   - **SSDs (Solid State Drives):**
     - Flash memory with no moving parts.
     - Faster access times and better random read/write performance but generally more expensive.

3. **I/O Patterns and Performance:**
   - **Sequential vs. Random I/O:**
     - Sequential I/O is faster because it minimizes seek time and rotational latency.
     - Random I/O can be slower due to higher seek times.
   - **Read and Write Amplification:**
     - Refers to the additional I/O operations required to perform a single logical read or write operation.
     - Common in SSDs due to the need to erase blocks before writing.

### Detailed Breakdown

1. **Page-Based Storage:**
   - **Pages:**
     - Fundamental units of data storage, typically 4KB to 16KB in size.
     - Designed to match the underlying hardware's block size for efficient I/O operations.
   - **Page Management:**
     - Efficient management is crucial for performance.
     - Pages may contain data records, index entries, or metadata.
   - **Buffer Pool:**
     - In-memory cache that holds recently accessed pages to reduce disk I/O.

2. **B-Trees and Variants:**
   - **B-Tree:**
     - Balanced tree data structure optimized for read and write operations on disk.
     - Nodes contain multiple keys and pointers, reducing the number of I/O operations required to find data.
   - **B+ Tree:**
     - Variation of B-Tree where all values are stored at the leaf level.
     - Internal nodes contain only keys and pointers, making range queries more efficient.
   - **Structure:**
     - Root, internal nodes, and leaf nodes.
     - Nodes split and merge to maintain balance as data is inserted or deleted.
   - **Operations:**
     - **Insertion:** Adds keys to the appropriate node, splitting nodes if necessary.
     - **Deletion:** Removes keys and merges nodes if necessary.
     - **Search:** Navigates from the root to the leaf node containing the key.

3. **Log-Structured Merge (LSM) Trees:**
   - **Concept:**
     - Designed for write-intensive workloads.
     - Data is initially written to an in-memory structure (memtable) and periodically flushed to disk (SSTable).
   - **Structure:**
     - **Memtable:** In-memory write buffer.
     - **SSTable:** Immutable disk-based storage of sorted data.
     - **Compaction:** Process of merging and compacting SSTables to reclaim space and improve read performance.
   - **Operations:**
     - **Write:** Data is written to the memtable, which is flushed to SSTables when full.
     - **Read:** Searches memtable first, then SSTables.
     - **Compaction:** Merges SSTables, discarding deleted entries and consolidating data.

4. **File Formats and Data Layout:**
   - **Row-Oriented Storage:**
     - Stores data row by row, making it efficient for transactional workloads (OLTP).
   - **Column-Oriented Storage:**
     - Stores data column by column, optimized for analytical workloads (OLAP).
   - **Hybrid Approaches:**
     - Combine row and columnar storage to balance read/write performance and storage efficiency.

5. **WAL (Write-Ahead Logging):**
   - **Purpose:**
     - Ensures data integrity by writing changes to a log before applying them to the database.
   - **Process:**
     - Write operations are logged before being applied to the data store.
     - In case of a crash, the log can be replayed to recover the database to a consistent state.

### Practical Examples

1. **B+ Tree Insertion Example:**
   - **Source Code:**
     ```java
     public class BPlusTree {
         private static final int T = 3; // B+ Tree order
         private Node root;

         class Node {
             int[] keys = new int[2 * T - 1];
             Node[] children = new Node[2 * T];
             int n;
             boolean leaf = true;

             void insertNonFull(int key) {
                 int i = n - 1;
                 if (leaf) {
                     while (i >= 0 && keys[i] > key) {
                         keys[i + 1] = keys[i];
                         i--;
                     }
                     keys[i + 1] = key;
                     n++;
                 } else {
                     while (i >= 0 && keys[i] > key) {
                         i--;
                     }
                     i++;
                     if (children[i].n == 2 * T - 1) {
                         splitChild(i, children[i]);
                         if (keys[i] < key) {
                             i++;
                         }
                     }
                     children[i].insertNonFull(key);
                 }
             }

             void splitChild(int i, Node y) {
                 Node z = new Node();
                 z.leaf = y.leaf;
                 z.n = T - 1;
                 for (int j = 0; j < T - 1; j++) {
                     z.keys[j] = y.keys[j + T];
                 }
                 if (!y.leaf) {
                     for (int j = 0; j < T; j++) {
                         z.children[j] = y.children[j + T];
                     }
                 }
                 y.n = T - 1;
                 for (int j = n; j >= i + 1; j--) {
                     children[j + 1] = children[j];
                 }
                 children[i + 1] = z;
                 for (int j = n - 1; j >= i; j--) {
                     keys[j + 1] = keys[j];
                 }
                 keys[i] = y.keys[T - 1];
                 n++;
             }
         }

         public BPlusTree() {
             root = new Node();
         }

         public void insert(int key) {
             Node r = root;
             if (r.n == 2 * T - 1) {
                 Node s = new Node();
                 root = s;
                 s.leaf = false;
                 s.children[0] = r;
                 s.splitChild(0, r);
                 s.insertNonFull(key);
             } else {
                 r.insertNonFull(key);
             }
         }
     }
     ```
   - **Usage:**
     ```java
     public class BPlusTreeExample {
         public static void main(String[] args) {
             BPlusTree tree = new BPlusTree();
             tree.insert(10);
             tree.insert(20);
             tree.insert(5);
             tree.insert(6);
             tree.insert(12);
             tree.insert(30);
             tree.insert(7);
             tree.insert(17);
         }
     }
     ```

2. **LSM Tree Write Operation Example:**
   - **Concept:**
     - Write data to the memtable, flush to SSTable when full, and perform compaction.
   - **Source Code:**
     ```java
     import java.util.*;
     import java.io.*;

     class Memtable {
         private TreeMap<String, String> map = new TreeMap<>();

         public void put(String key, String value) {
             map.put(key, value);
         }

         public String get(String key) {
             return map.get(key);
         }

         public void flush(String fileName) throws IOException {
             try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
                 for (Map.Entry<String, String> entry : map.entrySet()) {
                     writer.write(entry.getKey() + "," + entry.getValue());
                     writer.newLine();
                 }
             }
             map.clear();
         }
     }

     class SSTable {
         private TreeMap<String, String> map = new TreeMap<>();

         public SSTable(String fileName) throws IOException {
             try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
                 String line;
                 while ((line = reader.readLine()) != null) {
                     String[] parts = line.split(",");
                     map.put(parts[0], parts[1]);
                 }
             }
         }

         public String get(String key) {
             return map.get(key);
         }
     }

     public class LSMTreeExample {
         public static void main(String[] args) {
             try {
                 Memtable memtable = new Memtable();
                 memtable.put("a", "1");
                 memtable.put("b", "2");
                 memtable.put("c", "3");
                 memtable.flush("sstable1.txt");

                 SSTable sstable = new SSTable("sstable1.txt");
                 System.out.println("Value for key 'a': " + sstable.get("a"));
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }
     ```
   - **Output:**
     ```
     Value for key 'a': 1
     ```

3. **WAL (Write-Ahead Logging) Example:**
   - **Concept:**
     - Write changes to a log before applying them to ensure data integrity.
   - **Source Code:**
     ```java
     import java.io.*;
     import java.util.*;

     class WAL {
         private List<String> log = new ArrayList<>();

         public void write(String entry) {
             log.add(entry);
         }

         public void flush(String fileName) throws IOException {
             try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {
                 for (String entry : log) {
                     writer.write(entry);
                     writer.newLine();
                 }
             }
             log.clear();
         }
     }

     public class WALExample {
         public static void main(String[] args) {
             WAL wal = new WAL();
             wal.write("INSERT INTO table VALUES (1, 'a')");
             wal.write("INSERT INTO table VALUES (2, 'b')");
             wal.write("UPDATE table SET value='c' WHERE id=1");

             try {
                 wal.flush("wal.log");
                 System.out.println("WAL flushed to disk.");
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }
     ```
   - **Output:**
     ```
     WAL flushed to disk.
     ```

### Key Points to Remember

- **Disk-Based Storage:** Essential for handling large datasets and ensuring data durability.
- **Page-Based Storage:** Pages are the fundamental units of storage, and efficient management is crucial for performance.
- **B-Trees and LSM Trees:** Two primary data structures for organizing and accessing data on disk, each optimized for different workloads.
- **WAL (Write-Ahead Logging):** Ensures data integrity by logging changes before applying them.

### Summary

- **Disk-Based Storage:** Crucial for persisting large volumes of data and ensuring durability across system restarts.
- **Data Structures and File Formats:** Tailored to leverage the speed of disk storage while optimizing read/write performance.
- **WAL and Concurrency Control:** Provide mechanisms to ensure data integrity and handle concurrent operations efficiently.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 4 of "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov. For more in-depth explanations and additional exercises, refer to the full text of the book.