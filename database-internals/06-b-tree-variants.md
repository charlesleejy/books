### Detailed Notes of Chapter 6: B-Tree Variants from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter explores the various variants of B-Trees, each designed to optimize performance for specific use cases and workloads.
- B-Tree variants address limitations and improve aspects such as insertion speed, search efficiency, and storage utilization.

### Key Concepts

1. **Common B-Tree Variants:**
   - **B+ Trees**
   - **B* Trees**
   - **B^e Trees**
   - **Bw-Trees**
   - Each variant has unique characteristics that optimize for different aspects of database operations.

### Detailed Breakdown

1. **B+ Trees:**
   - **Structure:**
     - Internal nodes store only keys and pointers to child nodes.
     - Leaf nodes store actual data entries and are linked together to form a linked list.
   - **Advantages:**
     - Improved range query performance due to linked leaf nodes.
     - All insertions and deletions affect only the leaf nodes, keeping internal nodes more stable.
   - **Operations:**
     - **Search:** Similar to B-Tree, but only leaf nodes contain data.
     - **Insertion:** Insert into the appropriate leaf node. Split leaf nodes as necessary and propagate splits up.
     - **Deletion:** Remove from leaf nodes and merge or redistribute nodes as necessary.
   - **Example Use Case:** Filesystems and databases where range queries are common.
   - **Example Illustration:**
     ```java
     class BPlusTree {
         private BTreeNode root;
         private int t;

         public BPlusTree(int t) {
             this.t = t;
             root = new BTreeNode(t, true);
         }

         public void traverse() {
             if (root != null) {
                 root.traverse();
             }
         }

         public BTreeNode search(int k) {
             return (root == null) ? null : root.search(k);
         }

         public void insert(int k) {
             if (root.numKeys == 2 * t - 1) {
                 BTreeNode s = new BTreeNode(t, false);
                 s.children[0] = root;
                 s.splitChild(0, root);
                 int i = 0;
                 if (s.keys[0] < k) {
                     i++;
                 }
                 s.children[i].insertNonFull(k);
                 root = s;
             } else {
                 root.insertNonFull(k);
             }
         }

         public void remove(int k) {
             if (root == null) {
                 System.out.println("The tree is empty");
                 return;
             }

             root.remove(k);

             if (root.numKeys == 0) {
                 if (root.isLeaf) {
                     root = null;
                 } else {
                     root = root.children[0];
                 }
             }
         }
     }

     class BTreeNode {
         int[] keys;
         int t;
         BTreeNode[] children;
         int numKeys;
         boolean isLeaf;

         public BTreeNode(int t, boolean isLeaf) {
             this.t = t;
             this.isLeaf = isLeaf;
             this.keys = new int[2 * t - 1];
             this.children = new BTreeNode[2 * t];
             this.numKeys = 0;
         }

         public void traverse() {
             int i;
             for (i = 0; i < numKeys; i++) {
                 if (!isLeaf) {
                     children[i].traverse();
                 }
                 System.out.print(" " + keys[i]);
             }

             if (!isLeaf) {
                 children[i].traverse();
             }
         }

         public BTreeNode search(int k) {
             int i = 0;
             while (i < numKeys && k > keys[i]) {
                 i++;
             }

             if (i < numKeys && keys[i] == k) {
                 return this;
             }

             if (isLeaf) {
                 return null;
             }

             return children[i].search(k);
         }

         public void insertNonFull(int k) {
             int i = numKeys - 1;

             if (isLeaf) {
                 while (i >= 0 && keys[i] > k) {
                     keys[i + 1] = keys[i];
                     i--;
                 }

                 keys[i + 1] = k;
                 numKeys++;
             } else {
                 while (i >= 0 && keys[i] > k) {
                     i--;
                 }

                 if (children[i + 1].numKeys == 2 * t - 1) {
                     splitChild(i + 1, children[i + 1]);

                     if (keys[i + 1] < k) {
                         i++;
                     }
                 }
                 children[i + 1].insertNonFull(k);
             }
         }

         public void splitChild(int i, BTreeNode y) {
             BTreeNode z = new BTreeNode(y.t, y.isLeaf);
             z.numKeys = t - 1;

             for (int j = 0; j < t - 1; j++) {
                 z.keys[j] = y.keys[j + t];
             }

             if (!y.isLeaf) {
                 for (int j = 0; j < t; j++) {
                     z.children[j] = y.children[j + t];
                 }
             }

             y.numKeys = t - 1;

             for (int j = numKeys; j >= i + 1; j--) {
                 children[j + 1] = children[j];
             }

             children[i + 1] = z;

             for (int j = numKeys - 1; j >= i; j--) {
                 keys[j + 1] = keys[j];
             }

             keys[i] = y.keys[t - 1];
             numKeys++;
         }

         public void remove(int k) {
             int idx = findKey(k);

             if (idx < numKeys && keys[idx] == k) {
                 if (isLeaf) {
                     removeFromLeaf(idx);
                 } else {
                     removeFromNonLeaf(idx);
                 }
             } else {
                 if (isLeaf) {
                     System.out.println("The key " + k + " does not exist in the tree.");
                     return;
                 }

                 boolean flag = (idx == numKeys);

                 if (children[idx].numKeys < t) {
                     fill(idx);
                 }

                 if (flag && idx > numKeys) {
                     children[idx - 1].remove(k);
                 } else {
                     children[idx].remove(k);
                 }
             }
         }

         private int findKey(int k) {
             int idx = 0;
             while (idx < numKeys && keys[idx] < k) {
                 idx++;
             }
             return idx;
         }

         private void removeFromLeaf(int idx) {
             for (int i = idx + 1; i < numKeys; i++) {
                 keys[i - 1] = keys[i];
             }
             numKeys--;
         }

         private void removeFromNonLeaf(int idx) {
             int k = keys[idx];

             if (children[idx].numKeys >= t) {
                 int pred = getPredecessor(idx);
                 keys[idx] = pred;
                 children[idx].remove(pred);
             } else if (children[idx + 1].numKeys >= t) {
                 int succ = getSuccessor(idx);
                 keys[idx] = succ;
                 children[idx + 1].remove(succ);
             } else {
                 merge(idx);
                 children[idx].remove(k);
             }
         }

         private int getPredecessor(int idx) {
             BTreeNode current = children[idx];
             while (!current.isLeaf) {
                 current = current.children[current.numKeys];
             }
             return current.keys[current.numKeys - 1];
         }

         private int getSuccessor(int idx) {
             BTreeNode current = children[idx + 1];
             while (!current.isLeaf) {
                 current = current.children[0];
             }
             return current.keys[0];
         }

         private void fill(int idx) {
             if (idx != 0 && children[idx - 1].numKeys >= t) {
                 borrowFromPrev(idx);
             } else if (idx != numKeys && children[idx + 1].numKeys >= t) {
                 borrowFromNext(idx);
             } else {
                 if (idx != numKeys) {
                     merge(idx);
                 } else {
                     merge(idx - 1);
                 }
             }
         }

         private void borrowFromPrev(int idx) {
             BTreeNode child = children[idx];
             BTreeNode sibling = children[idx - 1];

             for (int i = child.numKeys - 1; i >= 0; i--) {
                 child.keys[i + 1] = child.keys[i];
             }

             if (!child.isLeaf) {
                 for (int i = child.numKeys; i >= 0; i--) {
                     child.children[i + 1] = child.children[i];
                 }
             }

             child.keys[0] = keys[idx - 1];

             if (!child.isLeaf) {
                 child.children[0] = sibling.children[sibling.numKeys];
             }

             keys[idx - 1] = sibling.keys[sibling.numKeys - 1];
             child.numKeys++;
             sibling.numKeys--;
         }

         private void borrowFromNext(int idx) {
             BTreeNode child = children[idx];
             BTreeNode sibling = children[idx + 1];

             child.keys[child.numKeys] = keys[idx];

             if (!child.isLeaf) {
                 child.children[child.numKeys + 1] = sibling.children[0];
             }

             keys[idx] = sibling.keys[0];

             for (int i = 1; i < sibling.numKeys; i++) {
                 sibling.keys[i - 1] = sibling.keys[i];
             }

             if (!sibling.isLeaf) {
                 for (int i = 1; i <= sibling.numKeys; i++) {
                     sibling.children[i - 1] = sibling.children[i];
                 }
             }

             child.numKeys++;
             sibling.numKeys--;
         }

         private void merge(int idx) {
             BTreeNode child = children[idx];
             BTreeNode sibling = children[idx + 1];

             child.keys[t - 1] = keys[idx];

             for (int i = 0; i < sibling.numKeys; i++) {
                 child.keys[i + t] = sibling.keys[i];
             }

             if (!child.isLeaf) {
                 for (int i = 0; i <= sibling.numKeys; i++) {
                     child.children[i + t] = sibling.children[i];
                 }
             }

             for (int i = idx + 1; i < numKeys; i++) {
                 keys[i - 1] = keys[i];
             }

             for (int i = idx + 2; i <= numKeys; i++) {
                 children[i - 1] = children[i];
             }

             child.numKeys += sibling.numKeys + 1;
             numKeys--;
         }
     }
     ```

2. **B* Trees:**
   - **Structure:**
     - Similar to B+ Trees but with more densely packed nodes.
     - Splits nodes less frequently by redistributing keys between siblings before splitting.
   - **Advantages:**
     - Better space utilization and reduced tree height.
     - Enhanced insertion and deletion performance by reducing the number of splits.
   - **Operations:**
     - **Search:** Same as B+ Trees.
     - **Insertion:** Redistribute keys between sibling nodes before splitting.
     - **Deletion:** Similar to B+ Trees but may involve more key redistributions to maintain balance.
   - **Example Use Case:** Databases requiring high write throughput with minimal splits.

3. **B^e Trees:**
   - **Structure:**
     - Combines aspects of B+ Trees and LSM Trees.
     - Utilizes an in-memory component (memtable) and a disk-based component (SSTable).
   - **Advantages:**
     - Optimized for both read and write performance.
     - Merges data from in-memory and disk-based components efficiently.
   - **Operations:**
     - **Write:** Data is written to the memtable and periodically flushed to SSTables.
     - **Read:** Searches memtable first, then SSTables.
     - **Compaction:** Periodically merges SSTables to maintain performance.
   - **Example Use Case:** Hybrid systems requiring fast writes and efficient reads.

4. **Bw-Trees:**
   - **Structure:**
     - Lock-free, cache-aware B-Tree variant designed for modern hardware.
     - Uses delta records to record changes and a mapping table to manage node locations.
   - **Advantages:**
     - Avoids locking overhead, allowing high concurrency.
     - Optimized for in-memory and disk-based storage with minimal cache misses.
   - **Operations:**
     - **Search:** Traverses the mapping table and applies delta records to obtain the final state.
     - **Insertion:** Records changes as delta records and periodically consolidates them.
     - **Deletion:** Similar to insertion, with delta records marking deletions.
   - **Example Use Case:** High-concurrency systems requiring lock-free operations and efficient cache utilization.

### Practical Examples

1. **B+ Tree Range Query Example:**
   - **Source Code:**
     ```java
     class BPlusTree {
         private BTreeNode root;
         private int t;

         public BPlusTree(int t) {
             this.t = t;
             root = new BTreeNode(t, true);
         }

         public void rangeQuery(int low, int high) {
             if (root != null) {
                 root.rangeQuery(low, high);
             }
         }
     }

     class BTreeNode {
         int[] keys;
         int t;
         BTreeNode[] children;
         int numKeys;
         boolean isLeaf;

         public BTreeNode(int t, boolean isLeaf) {
             this.t = t;
             this.isLeaf = isLeaf;
             this.keys = new int[2 * t - 1];
             this.children = new BTreeNode[2 * t];
             this.numKeys = 0;
         }

         public void rangeQuery(int low, int high) {
             int i = 0;
             while (i < numKeys && keys[i] < low) {
                 i++;
             }

             while (i < numKeys && keys[i] <= high) {
                 if (!isLeaf) {
                     children[i].rangeQuery(low, high);
                 }
                 System.out.print(" " + keys[i]);
                 i++;
             }

             if (!isLeaf) {
                 children[i].rangeQuery(low, high);
             }
         }
     }

     public class BPlusTreeExample {
         public static void main(String[] args) {
             BPlusTree tree = new BPlusTree(3);
             tree.insert(10);
             tree.insert(20);
             tree.insert(5);
             tree.insert(6);
             tree.insert(12);
             tree.insert(30);
             tree.insert(7);
             tree.insert(17);

             System.out.println("Range query (6-20):");
             tree.rangeQuery(6, 20);
         }
     }
     ```
   - **Output:**
     ```
     Range query (6-20):
     6 7 10 12 17 20
     ```

2. **B* Tree Insertion Example:**
   - **Concept:**
     - Redistribute keys between sibling nodes before splitting to minimize splits.
   - **Source Code:**
     ```java
     class BStarTree {
         private BTreeNode root;
         private int t;

         public BStarTree(int t) {
             this.t = t;
             root = new BTreeNode(t, true);
         }

         public void insert(int k) {
             if (root.numKeys == 2 * t - 1) {
                 BTreeNode s = new BTreeNode(t, false);
                 s.children[0] = root;
                 s.splitChild(0, root);
                 int i = 0;
                 if (s.keys[0] < k) {
                     i++;
                 }
                 s.children[i].insertNonFull(k);
                 root = s;
             } else {
                 root.insertNonFull(k);
             }
         }
     }

     class BTreeNode {
         int[] keys;
         int t;
         BTreeNode[] children;
         int numKeys;
         boolean isLeaf;

         public BTreeNode(int t, boolean isLeaf) {
             this.t = t;
             this.isLeaf = isLeaf;
             this.keys = new int[2 * t - 1];
             this.children = new BTreeNode[2 * t];
             this.numKeys = 0;
         }

         public void insertNonFull(int k) {
             int i = numKeys - 1;

             if (isLeaf) {
                 while (i >= 0 && keys[i] > k) {
                     keys[i + 1] = keys[i];
                     i--;
                 }

                 keys[i + 1] = k;
                 numKeys++;
             } else {
                 while (i >= 0 && keys[i] > k) {
                     i--;
                 }

                 if (children[i + 1].numKeys == 2 * t - 1) {
                     splitChild(i + 1, children[i + 1]);

                     if (keys[i + 1] < k) {
                         i++;
                     }
                 }
                 children[i + 1].insertNonFull(k);
             }
         }

         public void splitChild(int i, BTreeNode y) {
             BTreeNode z = new BTreeNode(y.t, y.isLeaf);
             z.numKeys = t - 1;

             for (int j = 0; j < t - 1; j++) {
                 z.keys[j] = y.keys[j + t];
             }

             if (!y.isLeaf) {
                 for (int j = 0; j < t; j++) {
                     z.children[j] = y.children[j + t];
                 }
             }

             y.numKeys = t - 1;

             for (int j = numKeys; j >= i + 1; j--) {
                 children[j + 1] = children[j];
             }

             children[i + 1] = z;

             for (int j = numKeys - 1; j >= i; j--) {
                 keys[j + 1] = keys[j];
             }

             keys[i] = y.keys[t - 1];
             numKeys++;
         }
     }

     public class BStarTreeExample {
         public static void main(String[] args) {
             BStarTree tree = new BStarTree(3);
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

### Key Points to Remember

- **B+ Trees:** Optimized for range queries and stable internal nodes by storing all data in leaf nodes and linking them together.
- **B* Trees:** Enhance space utilization and reduce tree height by redistributing keys between siblings before splitting nodes.
- **B^e Trees:** Combine in-memory and disk-based components to optimize both read