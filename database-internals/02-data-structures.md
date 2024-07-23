### Detailed Notes of Chapter 2: Data Structures from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter explores the core data structures used in databases.
- Focuses on the principles, design, and implementation of data structures that support efficient data storage, retrieval, and management.

### Key Concepts

1. **Memory Hierarchy and Data Structures:**
   - **Memory Hierarchy:**
     - **Registers and Cache:** Fastest but smallest memory, used for temporary storage of frequently accessed data.
     - **Main Memory (RAM):** Larger and slower than cache, used for actively processed data.
     - **Secondary Storage (Disk/SSD):** Largest and slowest, used for long-term data storage.
   - **Data Structure Design:**
     - Must consider the trade-offs between speed, size, and persistence.
     - Efficient data structures minimize access time and optimize for the characteristics of the storage medium.

2. **Page-Based Storage:**
   - **Pages:**
     - Fundamental units of data storage in databases.
     - Typically 4KB to 16KB in size, designed to match the underlying hardware's block size.
   - **Page Management:**
     - Efficient page management is crucial for performance.
     - Pages may contain data records, index entries, or metadata.

3. **B-Trees and Variants:**
   - **B-Tree:**
     - Balanced tree data structure optimized for read and write operations.
     - Nodes contain multiple keys and pointers, reducing the number of I/O operations.
   - **B+ Tree:**
     - Variation of B-Tree where all values are at the leaf level.
     - Internal nodes contain only keys and pointers, making range queries more efficient.
   - **Structure:**
     - Root, internal nodes, and leaf nodes.
     - Nodes split and merge to maintain balance as data is inserted or deleted.
   - **Operations:**
     - **Insertion:** Adds keys to the appropriate node, splitting nodes if necessary.
     - **Deletion:** Removes keys and merges nodes if necessary.
     - **Search:** Navigates from the root to the leaf node containing the key.

4. **Log-Structured Merge (LSM) Trees:**
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

5. **Hash Tables:**
   - **Concept:**
     - Provides constant-time complexity for insert, delete, and search operations.
   - **Structure:**
     - Consists of an array of buckets, each storing a list of key-value pairs.
     - Uses a hash function to map keys to buckets.
   - **Operations:**
     - **Insertion:** Computes hash and adds the key-value pair to the corresponding bucket.
     - **Deletion:** Computes hash, finds the key in the bucket, and removes it.
     - **Search:** Computes hash and searches the corresponding bucket for the key.
   - **Collision Handling:**
     - **Chaining:** Stores colliding keys in a linked list within the same bucket.
     - **Open Addressing:** Finds an alternate location within the array using probing.

6. **Bitmaps and Bitmap Indexes:**
   - **Concept:**
     - Efficiently represents and queries boolean data or categorical data with a limited number of distinct values.
   - **Structure:**
     - Bitmap is an array of bits where each bit represents the presence or absence of a value.
   - **Operations:**
     - **AND, OR, NOT:** Bitwise operations on bitmaps to perform set operations.
     - **Compression:** Techniques such as Run-Length Encoding (RLE) to reduce the size of bitmaps.

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

### Key Points to Remember

- **Data Structure Design:** Efficient data structures are crucial for optimizing performance in databases.
- **Page-Based Storage:** Pages are fundamental units of storage, and efficient management of pages is essential.
-