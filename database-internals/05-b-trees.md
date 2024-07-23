### Detailed Notes of Chapter 5: B-Trees from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter focuses on B-Trees, a fundamental data structure used in many databases to efficiently store and retrieve data.
- B-Trees are balanced tree data structures that maintain sorted data and allow searches, sequential access, insertions, and deletions in logarithmic time.

### Key Concepts

1. **B-Tree Basics:**
   - **Definition:** A balanced tree data structure that maintains sorted order and allows for efficient insertion, deletion, and search operations.
   - **Properties:**
     - All leaves are at the same depth.
     - Internal nodes can have a variable number of child nodes within a pre-defined range.
     - B-Trees minimize disk reads and writes by maximizing the number of keys stored in each node, which reduces the tree height and the number of I/O operations.

2. **Structure of B-Trees:**
   - **Nodes:**
     - Each node contains multiple keys and child pointers.
     - Nodes have a minimum and maximum number of keys they can hold, typically defined by the order of the B-Tree.
   - **Order (t):**
     - Defines the minimum degree of the tree.
     - Each node (except the root) must have at least t-1 keys and can have at most 2t-1 keys.
     - The root node must have at least 1 key and can have at most 2t-1 keys.

3. **Operations:**
   - **Search:**
     - Begins at the root and recursively traverses the tree to find the key.
     - At each node, a binary search is performed on the keys to determine the next child to visit.
   - **Insertion:**
     - Keys are inserted in sorted order.
     - If a node overflows (i.e., exceeds the maximum number of keys), it is split, and the middle key is promoted to the parent node.
     - Splitting propagates up the tree, maintaining balance.
   - **Deletion:**
     - Keys can be deleted directly if the node still has enough keys.
     - If a node underflows (i.e., falls below the minimum number of keys), keys are borrowed from or merged with neighboring nodes to maintain balance.

### Detailed Breakdown

1. **B-Tree Node Structure:**
   - **Components:**
     - Keys: Stored in sorted order within each node.
     - Children: Pointers to child nodes, used to navigate the tree.
   - **Example:**
     ```java
     class BTreeNode {
         int[] keys; // Array of keys
         BTreeNode[] children; // Array of child pointers
         int numKeys; // Number of keys in the node
         boolean isLeaf; // True if the node is a leaf

         BTreeNode(int t) {
             keys = new int[2 * t - 1];
             children = new BTreeNode[2 * t];
             numKeys = 0;
             isLeaf = true;
         }
     }
     ```

2. **Search Operation:**
   - **Process:**
     - Start at the root and perform a binary search on the keys.
     - If the key is found, return the key.
     - If the key is not found and the node is a leaf, the key does not exist.
     - If the node is not a leaf, recursively search the appropriate child.
   - **Example:**
     ```java
     class BTree {
         private BTreeNode root;
         private int t;

         BTree(int t) {
             this.t = t;
             root = new BTreeNode(t);
         }

         public BTreeNode search(int key) {
             return search(root, key);
         }

         private BTreeNode search(BTreeNode node, int key) {
             int i = 0;
             while (i < node.numKeys && key > node.keys[i]) {
                 i++;
             }
             if (i < node.numKeys && key == node.keys[i]) {
                 return node;
             }
             if (node.isLeaf) {
                 return null;
             } else {
                 return search(node.children[i], key);
             }
         }
     }
     ```

3. **Insertion Operation:**
   - **Process:**
     - Insert the key in the appropriate node while maintaining sorted order.
     - If a node overflows, split it into two nodes, and promote the middle key to the parent.
     - Splitting may propagate up to the root, potentially increasing the tree height.
   - **Example:**
     ```java
     class BTree {
         private BTreeNode root;
         private int t;

         BTree(int t) {
             this.t = t;
             root = new BTreeNode(t);
         }

         public void insert(int key) {
             BTreeNode r = root;
             if (r.numKeys == 2 * t - 1) {
                 BTreeNode s = new BTreeNode(t);
                 root = s;
                 s.isLeaf = false;
                 s.numKeys = 0;
                 s.children[0] = r;
                 splitChild(s, 0, r);
                 insertNonFull(s, key);
             } else {
                 insertNonFull(r, key);
             }
         }

         private void splitChild(BTreeNode x, int i, BTreeNode y) {
             BTreeNode z = new BTreeNode(t);
             z.isLeaf = y.isLeaf;
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
             for (int j = x.numKeys; j >= i + 1; j--) {
                 x.children[j + 1] = x.children[j];
             }
             x.children[i + 1] = z;
             for (int j = x.numKeys - 1; j >= i; j--) {
                 x.keys[j + 1] = x.keys[j];
             }
             x.keys[i] = y.keys[t - 1];
             x.numKeys++;
         }

         private void insertNonFull(BTreeNode x, int k) {
             int i = x.numKeys - 1;
             if (x.isLeaf) {
                 while (i >= 0 && k < x.keys[i]) {
                     x.keys[i + 1] = x.keys[i];
                     i--;
                 }
                 x.keys[i + 1] = k;
                 x.numKeys++;
             } else {
                 while (i >= 0 && k < x.keys[i]) {
                     i--;
                 }
                 i++;
                 if (x.children[i].numKeys == 2 * t - 1) {
                     splitChild(x, i, x.children[i]);
                     if (k > x.keys[i]) {
                         i++;
                     }
                 }
                 insertNonFull(x.children[i], k);
             }
         }
     }
     ```

4. **Deletion Operation:**
   - **Process:**
     - Locate the key to be deleted.
     - If the key is in a leaf node, remove it directly.
     - If the key is in an internal node, replace it with its predecessor or successor and recursively delete the predecessor or successor.
     - Ensure that the tree remains balanced by borrowing keys from or merging nodes as necessary.
   - **Example:**
     ```java
     class BTree {
         private BTreeNode root;
         private int t;

         BTree(int t) {
             this.t = t;
             root = new BTreeNode(t);
         }

         public void delete(int key) {
             delete(root, key);
             if (root.numKeys == 0) {
                 root = root.isLeaf ? null : root.children[0];
             }
         }

         private void delete(BTreeNode node, int key) {
             int idx = findKey(node, key);

             if (idx < node.numKeys && node.keys[idx] == key) {
                 if (node.isLeaf) {
                     removeFromLeaf(node, idx);
                 } else {
                     removeFromNonLeaf(node, idx);
                 }
             } else {
                 if (node.isLeaf) {
                     return;
                 }
                 boolean flag = (idx == node.numKeys);
                 if (node.children[idx].numKeys < t) {
                     fill(node, idx);
                 }
                 if (flag && idx > node.numKeys) {
                     delete(node.children[idx - 1], key);
                 } else {
                     delete(node.children[idx], key);
                 }
             }
         }

         private int findKey(BTreeNode node, int key) {
             int idx = 0;
             while (idx < node.numKeys && node.keys[idx] < key) {
                 idx++;
             }
             return idx;
         }

         private void removeFromLeaf(BTreeNode node, int idx) {
             for (int i = idx + 1; i < node.numKeys; i++) {
                 node.keys[i - 1] = node.keys[i];
             }
             node.numKeys--;
         }

         private void removeFromNonLeaf(BTreeNode node, int idx) {
             int key = node.keys[idx];
             if (node.children[idx].numKeys >= t) {
                 int pred = getPredecessor(node, idx);
                 node.keys[idx] = pred;
                 delete(node.children[idx], pred);
             } else if (node



             .children[idx + 1].numKeys >= t) {
                 int succ = getSuccessor(node, idx);
                 node.keys[idx] = succ;
                 delete(node.children[idx + 1], succ);
             } else {
                 merge(node, idx);
                 delete(node.children[idx], key);
             }
         }

         private int getPredecessor(BTreeNode node, int idx) {
             BTreeNode current = node.children[idx];
             while (!current.isLeaf) {
                 current = current.children[current.numKeys];
             }
             return current.keys[current.numKeys - 1];
         }

         private int getSuccessor(BTreeNode node, int idx) {
             BTreeNode current = node.children[idx + 1];
             while (!current.isLeaf) {
                 current = current.children[0];
             }
             return current.keys[0];
         }

         private void fill(BTreeNode node, int idx) {
             if (idx != 0 && node.children[idx - 1].numKeys >= t) {
                 borrowFromPrev(node, idx);
             } else if (idx != node.numKeys && node.children[idx + 1].numKeys >= t) {
                 borrowFromNext(node, idx);
             } else {
                 if (idx != node.numKeys) {
                     merge(node, idx);
                 } else {
                     merge(node, idx - 1);
                 }
             }
         }

         private void borrowFromPrev(BTreeNode node, int idx) {
             BTreeNode child = node.children[idx];
             BTreeNode sibling = node.children[idx - 1];

             for (int i = child.numKeys - 1; i >= 0; i--) {
                 child.keys[i + 1] = child.keys[i];
             }
             if (!child.isLeaf) {
                 for (int i = child.numKeys; i >= 0; i--) {
                     child.children[i + 1] = child.children[i];
                 }
             }
             child.keys[0] = node.keys[idx - 1];
             if (!child.isLeaf) {
                 child.children[0] = sibling.children[sibling.numKeys];
             }
             node.keys[idx - 1] = sibling.keys[sibling.numKeys - 1];
             child.numKeys++;
             sibling.numKeys--;
         }

         private void borrowFromNext(BTreeNode node, int idx) {
             BTreeNode child = node.children[idx];
             BTreeNode sibling = node.children[idx + 1];

             child.keys[child.numKeys] = node.keys[idx];
             if (!child.isLeaf) {
                 child.children[child.numKeys + 1] = sibling.children[0];
             }
             node.keys[idx] = sibling.keys[0];
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

         private void merge(BTreeNode node, int idx) {
             BTreeNode child = node.children[idx];
             BTreeNode sibling = node.children[idx + 1];

             child.keys[t - 1] = node.keys[idx];
             for (int i = 0; i < sibling.numKeys; i++) {
                 child.keys[i + t] = sibling.keys[i];
             }
             if (!child.isLeaf) {
                 for (int i = 0; i <= sibling.numKeys; i++) {
                     child.children[i + t] = sibling.children[i];
                 }
             }
             for (int i = idx + 1; i < node.numKeys; i++) {
                 node.keys[i - 1] = node.keys[i];
             }
             for (int i = idx + 2; i <= node.numKeys; i++) {
                 node.children[i - 1] = node.children[i];
             }
             child.numKeys += sibling.numKeys + 1;
             node.numKeys--;
         }
     }
     ```

### Practical Examples

1. **B-Tree Implementation Example:**
   - **Source Code:**
     ```java
     public class BTree {
         private BTreeNode root;
         private int t;

         public BTree(int t) {
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
                 keys[i - 1] =


                  keys[i];
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

### Key Points to Remember

- **B-Trees:** Balanced tree data structures optimized for disk storage, allowing efficient insertion, deletion, and search operations.
- **Structure:** Nodes contain multiple keys and child pointers, and nodes split and merge to maintain balance.
- **Operations:**
  - **Search:** Efficiently locate keys using binary search and traversal.
  - **Insertion:** Insert keys while maintaining order, and split nodes when necessary.
  - **Deletion:** Remove keys and rebalance the tree by borrowing or merging nodes as necessary.

### Summary

- **B-Trees:** Fundamental data structures in many databases, providing efficient storage and retrieval of data.
- **Balanced Structure:** Ensures that the tree remains balanced, minimizing the height and reducing the number of I/O operations.
- **Efficient Operations:** Support logarithmic time complexity for search, insertion, and deletion, making B-Trees suitable for large datasets stored on disk.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 5 of "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov. For more in-depth explanations and additional exercises, refer to the full text of the book.