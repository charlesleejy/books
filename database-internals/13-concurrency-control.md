### Detailed Notes of Chapter 13: Concurrency Control from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter delves into concurrency control mechanisms in distributed databases, which are essential for maintaining consistency and ensuring that transactions are executed in a way that does not lead to conflicts.

### Key Concepts

1. **Concurrency Control:**
   - **Definition:** Techniques to ensure that multiple transactions can execute concurrently without leading to inconsistencies.
   - **Purpose:** To manage simultaneous operations on a database while maintaining data integrity.

2. **Goals of Concurrency Control:**
   - **Isolation:** Ensures that the operations of one transaction are isolated from those of others.
   - **Consistency:** Ensures that the database remains in a consistent state before and after transactions.
   - **Atomicity:** Ensures that transactions are all-or-nothing, even when multiple transactions are running concurrently.

### Detailed Breakdown

1. **Concurrency Control Techniques:**
   - **Pessimistic Concurrency Control:**
     - **Locks:** Transactions acquire locks to prevent other transactions from accessing the same data concurrently.
     - **Types of Locks:**
       - **Shared Locks (S-Locks):** Allow multiple transactions to read a data item but not modify it.
       - **Exclusive Locks (X-Locks):** Allow only one transaction to modify a data item.
     - **Deadlock Detection and Resolution:** Mechanisms to detect and resolve deadlocks where transactions wait indefinitely for each other to release locks.
       - **Example:**
         ```java
         class LockManager {
             private Map<String, Lock> lockTable = new HashMap<>();

             public synchronized void acquireLock(String resource, boolean exclusive) throws InterruptedException {
                 while (lockTable.containsKey(resource) && (exclusive || lockTable.get(resource).isExclusive())) {
                     wait();
                 }
                 lockTable.put(resource, new Lock(exclusive));
             }

             public synchronized void releaseLock(String resource) {
                 lockTable.remove(resource);
                 notifyAll();
             }
         }

         class Lock {
             private boolean exclusive;

             public Lock(boolean exclusive) {
                 this.exclusive = exclusive;
             }

             public boolean isExclusive() {
                 return exclusive;
             }
         }
         ```

   - **Optimistic Concurrency Control:**
     - **Validation:** Transactions execute without locking resources. Before committing, they validate that no other transactions have modified the data they accessed.
     - **Phases:**
       - **Read Phase:** Transactions read data and make tentative changes.
       - **Validation Phase:** Checks for conflicts with other transactions.
       - **Write Phase:** If validation passes, changes are committed.
     - **Example:**
       ```java
       class OptimisticTransaction {
           private Map<String, String> readSet = new HashMap<>();
           private Map<String, String> writeSet = new HashMap<>();
           private Database db;

           public OptimisticTransaction(Database db) {
               this.db = db;
           }

           public String read(String key) {
               if (writeSet.containsKey(key)) {
                   return writeSet.get(key);
               }
               String value = db.read(key);
               readSet.put(key, value);
               return value;
           }

           public void write(String key, String value) {
               writeSet.put(key, value);
           }

           public boolean commit() {
               for (String key : readSet.keySet()) {
                   if (!db.validate(key, readSet.get(key))) {
                       return false;
                   }
               }
               for (String key : writeSet.keySet()) {
                   db.write(key, writeSet.get(key));
               }
               return true;
           }
       }

       class Database {
           private Map<String, String> data = new HashMap<>();

           public synchronized String read(String key) {
               return data.get(key);
           }

           public synchronized boolean validate(String key, String expectedValue) {
               return data.get(key).equals(expectedValue);
           }

           public synchronized void write(String key, String value) {
               data.put(key, value);
           }
       }
       ```

2. **Multi-Version Concurrency Control (MVCC):**
   - **Concept:** Maintains multiple versions of data to allow transactions to access a consistent snapshot without locking.
   - **Read and Write Operations:**
     - **Reads:** Access the latest committed version of data as of the transaction start time.
     - **Writes:** Create a new version of data and maintain previous versions for other concurrent transactions.
   - **Garbage Collection:** Mechanism to remove obsolete versions of data no longer needed by any transactions.
   - **Example:**
     ```java
     class MVCCDatabase {
         private Map<String, List<VersionedValue>> data = new HashMap<>();

         public String read(String key, long timestamp) {
             List<VersionedValue> versions = data.get(key);
             for (VersionedValue version : versions) {
                 if (version.timestamp <= timestamp) {
                     return version.value;
                 }
             }
             return null;
         }

         public void write(String key, String value, long timestamp) {
             List<VersionedValue> versions = data.getOrDefault(key, new ArrayList<>());
             versions.add(new VersionedValue(value, timestamp));
             data.put(key, versions);
         }

         public void garbageCollect(long oldestTimestamp) {
             for (List<VersionedValue> versions : data.values()) {
                 versions.removeIf(version -> version.timestamp < oldestTimestamp);
             }
         }
     }

     class VersionedValue {
         String value;
         long timestamp;

         VersionedValue(String value, long timestamp) {
             this.value = value;
             this.timestamp = timestamp;
         }
     }
     ```

3. **Snapshot Isolation:**
   - **Concept:** Provides a consistent snapshot of the database to each transaction, ensuring that transactions do not see changes made by others until they are committed.
   - **Advantages:** Prevents many concurrency anomalies, such as dirty reads and non-repeatable reads.
   - **Implementation:** Often achieved using MVCC.
   - **Example:**
     ```java
     class SnapshotIsolationTransaction {
         private MVCCDatabase db;
         private long timestamp;
         private Map<String, String> writeSet = new HashMap<>();

         public SnapshotIsolationTransaction(MVCCDatabase db, long timestamp) {
             this.db = db;
             this.timestamp = timestamp;
         }

         public String read(String key) {
             return db.read(key, timestamp);
         }

         public void write(String key, String value) {
             writeSet.put(key, value);
         }

         public void commit() {
             long commitTimestamp = System.currentTimeMillis();
             for (Map.Entry<String, String> entry : writeSet.entrySet()) {
                 db.write(entry.getKey(), entry.getValue(), commitTimestamp);
             }
         }
     }
     ```

4. **Serializable Snapshot Isolation:**
   - **Concept:** Extends snapshot isolation by ensuring that the serializability of transactions is maintained, preventing anomalies like write skew.
   - **Implementation:** Combines MVCC with additional checks to ensure serializable execution.
   - **Example:**
     ```java
     class SerializableSnapshotIsolationTransaction extends SnapshotIsolationTransaction {
         public SerializableSnapshotIsolationTransaction(MVCCDatabase db, long timestamp) {
             super(db, timestamp);
         }

         @Override
         public void commit() {
             // Additional checks for serializability
             super.commit();
         }
     }
     ```

### Practical Examples

1. **Pessimistic Concurrency Control Example:**
   - **Scenario:** Using locks to ensure data consistency.
   - **Example Implementation:**
     ```java
     class PessimisticTransaction {
         private LockManager lockManager;
         private Database db;

         public PessimisticTransaction(LockManager lockManager, Database db) {
             this.lockManager = lockManager;
             this.db = db;
         }

         public String read(String key) throws InterruptedException {
             lockManager.acquireLock(key, false);
             return db.read(key);
         }

         public void write(String key, String value) throws InterruptedException {
             lockManager.acquireLock(key, true);
             db.write(key, value);
             lockManager.releaseLock(key);
         }
     }

     class LockManager {
         private Map<String, Lock> lockTable = new HashMap<>();

         public synchronized void acquireLock(String resource, boolean exclusive) throws InterruptedException {
             while (lockTable.containsKey(resource) && (exclusive || lockTable.get(resource).isExclusive())) {
                 wait();
             }
             lockTable.put(resource, new Lock(exclusive));
         }

         public synchronized void releaseLock(String resource) {
             lockTable.remove(resource);
             notifyAll();
         }
     }

     class Lock {
         private boolean exclusive;

         public Lock(boolean exclusive) {
             this.exclusive = exclusive;
         }

         public boolean isExclusive() {
             return exclusive;
         }
     }

     class Database {
         private Map<String, String> data = new HashMap<>();

         public synchronized String read(String key) {
             return data.get(key);
         }

         public synchronized void write(String key, String value) {
             data.put(key, value);
         }
     }
     ```

2. **Optimistic Concurrency Control Example:**
   - **Scenario:** Using optimistic concurrency control to validate transactions before committing.
   - **Example Implementation:**
     ```java
     class OptimisticTransaction {
         private Map<String, String> readSet = new HashMap<>();
         private Map<String, String> writeSet = new HashMap<>();
         private Database db;

         public OptimisticTransaction(Database db) {
             this.db = db;
         }

         public String read(String key) {
             if (writeSet.containsKey(key)) {
                 return writeSet.get(key);
             }
             String value = db.read(key);
             readSet.put(key, value);
             return value;
         }

         public void write(String key, String value) {
             writeSet.put(key, value);
         }

         public boolean commit() {
             for (String key : readSet.keySet()) {
                 if (!db.validate(key, readSet.get(key))) {
                     return false;
                 }
             }
             for (String key : writeSet.keySet()) {
                 db.write(key, writeSet.get(key));
             }
             return true;
         }
     }

     class Database {
         private Map<String, String> data = new HashMap<>();

         public synchronized String read(String key) {
             return data.get(key);
         }

         public synchronized boolean validate(String key, String expectedValue) {
             return data.get(key).equals(expectedValue);
         }

         public synchronized void write(String key, String value) {
             data.put(key, value);
         }
     }
     ```

### Key Points to Remember

- **Concurrency Control:** Essential for maintaining data consistency and integrity in distributed systems.
- **Pessimistic vs. Optimistic Control:** Pessimistic control uses locks to prevent conflicts, while optimistic control validates transactions at commit time.
- **MVCC:** Allows transactions to access consistent snapshots without locking, improving concurrency.
- **Snapshot Isolation:** Provides a consistent view of the database to each transaction, preventing many concurrency anomalies.
- **Serializable Snapshot Isolation:** Ensures serializability by combining snapshot isolation with additional checks.

### Summary

- **Concurrency Control:** Ensures that multiple transactions can execute concurrently without leading to inconsistencies.
- **Techniques and Implementation:** Pessimistic and optimistic concurrency control, MVCC, and snapshot isolation provide various mechanisms to achieve concurrency control.
- **Trade-offs:** Each concurrency control mechanism has its trade-offs in terms of performance, complexity, and consistency guarantees.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 13 of "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov. For more in-depth explanations and additional exercises, refer to the full text of the book.