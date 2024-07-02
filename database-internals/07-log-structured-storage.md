### Detailed Notes of Chapter 7: Log-Structured Storage from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter explores log-structured storage systems, a method of storing data that optimizes write performance by treating the storage as an append-only log.
- Log-structured storage is particularly effective for write-intensive applications and modern SSDs, which have different performance characteristics compared to traditional HDDs.

### Key Concepts

1. **Log-Structured Storage Fundamentals:**
   - **Definition:** A storage system where all updates are appended to a sequential log, rather than updating data in place.
   - **Purpose:** To optimize write performance by avoiding random writes, which are slower on both HDDs and SSDs.

2. **Components:**
   - **Memtable:** An in-memory structure that holds recent writes.
   - **Immutable Memtable:** When the memtable is full, it becomes immutable and is written to disk as an SSTable.
   - **SSTables (Sorted String Tables):** Immutable, disk-based structures that store data in a sorted format.
   - **WAL (Write-Ahead Log):** A log that records all changes before they are applied to the memtable, ensuring durability.

### Detailed Breakdown

1. **Write Path:**
   - **Process:**
     - Write operations are first recorded in the WAL.
     - The data is then added to the memtable.
     - When the memtable reaches a certain size, it is flushed to disk as an SSTable.
   - **Advantages:**
     - Fast write performance due to sequential writes.
     - Data durability ensured by the WAL.

2. **Read Path:**
   - **Process:**
     - Read operations first check the memtable for the latest data.
     - If the data is not found in the memtable, the immutable memtables (recently flushed SSTables) are checked.
     - Finally, older SSTables on disk are checked.
   - **Optimization:**
     - Bloom filters and indexes can be used to quickly determine if an SSTable contains the requested data, reducing the need for disk reads.

3. **Compaction:**
   - **Purpose:** To merge SSTables and reclaim space, remove deleted data, and maintain read performance.
   - **Types of Compaction:**
     - **Minor Compaction:** Merges memtables and a few SSTables.
     - **Major Compaction:** Merges all SSTables, removing duplicates and deleted entries.
   - **Process:**
     - Identify SSTables for compaction.
     - Read data from these SSTables, merge, and write back to a new SSTable.
     - Delete old SSTables.

4. **Garbage Collection:**
   - **Purpose:** To remove outdated or deleted data from the storage.
   - **Process:**
     - During compaction, outdated data is identified and not included in the new SSTable.
     - Periodic cleanup operations may also be run to remove old WAL files and other obsolete data.

5. **Optimizations:**
   - **Bloom Filters:** Used to quickly check if an SSTable contains a specific key, reducing unnecessary disk reads.
   - **Partitioning:** Data can be partitioned to improve write and read performance, particularly in distributed systems.
   - **Compression:** Data in SSTables can be compressed to save space and reduce I/O overhead.

### Practical Examples

1. **Write Path Example:**
   - **Source Code:**
     ```java
     class LogStructuredStorage {
         private Memtable memtable;
         private List<SSTable> ssTables;
         private WriteAheadLog wal;

         public LogStructuredStorage() {
             memtable = new Memtable();
             ssTables = new ArrayList<>();
             wal = new WriteAheadLog();
         }

         public void write(String key, String value) {
             wal.log(key, value);
             memtable.put(key, value);
             if (memtable.isFull()) {
                 flushMemtable();
             }
         }

         private void flushMemtable() {
             SSTable sstable = memtable.flushToSSTable();
             ssTables.add(sstable);
             memtable = new Memtable();
         }
     }

     class WriteAheadLog {
         public void log(String key, String value) {
             // Append key-value to log file
         }
     }

     class Memtable {
         private Map<String, String> data;
         private static final int MAX_SIZE = 1000;

         public Memtable() {
             data = new TreeMap<>();
         }

         public void put(String key, String value) {
             data.put(key, value);
         }

         public boolean isFull() {
             return data.size() >= MAX_SIZE;
         }

         public SSTable flushToSSTable() {
             return new SSTable(data);
         }
     }

     class SSTable {
         private Map<String, String> data;

         public SSTable(Map<String, String> data) {
             this.data = new TreeMap<>(data);
             // Write data to disk
         }

         public String get(String key) {
             return data.get(key);
         }
     }
     ```

2. **Read Path Example:**
   - **Source Code:**
     ```java
     public String read(String key) {
         String value = memtable.get(key);
         if (value != null) {
             return value;
         }

         for (SSTable sstable : ssTables) {
             value = sstable.get(key);
             if (value != null) {
                 return value;
             }
         }
         return null;
     }

     class Memtable {
         private Map<String, String> data;

         public String get(String key) {
             return data.get(key);
         }
     }

     class SSTable {
         private Map<String, String> data;

         public String get(String key) {
             return data.get(key);
         }
     }
     ```

3. **Compaction Example:**
   - **Source Code:**
     ```java
     public void compact() {
         List<SSTable> newSSTables = new ArrayList<>();
         Map<String, String> mergedData = new TreeMap<>();

         for (SSTable sstable : ssTables) {
             mergedData.putAll(sstable.getData());
         }

         SSTable newSSTable = new SSTable(mergedData);
         newSSTables.add(newSSTable);

         // Delete old SSTables and replace with new ones
         ssTables = newSSTables;
     }

     class SSTable {
         private Map<String, String> data;

         public Map<String, String> getData() {
             return new TreeMap<>(data);
         }
     }
     ```

### Key Points to Remember

- **Log-Structured Storage:** Optimizes write performance by appending data to a sequential log.
- **Components:** Memtable, immutable memtable, SSTables, and WAL are crucial for ensuring fast writes and data durability.
- **Compaction:** Necessary to merge SSTables, reclaim space, and maintain read performance.
- **Optimizations:** Bloom filters, partitioning, and compression can enhance performance and efficiency.

### Summary

- **Log-Structured Storage:** Provides significant performance benefits for write-intensive applications by avoiding random writes and treating storage as an append-only log.
- **Write and Read Paths:** Efficiently handle data writes and reads through memtables, SSTables, and compaction processes.
- **Compaction and Garbage Collection:** Maintain storage efficiency and performance by merging data and removing outdated entries.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 7 of "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov. For more in-depth explanations and additional exercises, refer to the full text of the book.