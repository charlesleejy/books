### Detailed Notes of Chapter 8: Introduction to Distributed Systems from "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov

#### Overview
- This chapter introduces the fundamental concepts of distributed systems and their importance in modern database systems.
- Distributed systems allow databases to scale horizontally, providing high availability, fault tolerance, and improved performance.

### Key Concepts

1. **Distributed Systems Basics:**
   - **Definition:** A distributed system is a network of independent computers that work together to appear as a single coherent system.
   - **Purpose:** To provide high availability, fault tolerance, and scalability by distributing the workload across multiple machines.

2. **Challenges in Distributed Systems:**
   - **Consistency:** Ensuring that all nodes in the system have the same data at any given time.
   - **Availability:** Ensuring that the system is operational and can process requests even in the event of failures.
   - **Partition Tolerance:** Ensuring that the system continues to operate even if there are network partitions that separate nodes.
   - **CAP Theorem:** States that it is impossible for a distributed system to simultaneously provide all three of Consistency, Availability, and Partition Tolerance. Only two can be fully achieved at any given time.

### Detailed Breakdown

1. **Architecture of Distributed Systems:**
   - **Monolithic vs. Distributed:**
     - Monolithic systems run on a single machine and have limitations in scalability and fault tolerance.
     - Distributed systems spread the workload across multiple machines, providing better scalability and fault tolerance.
   - **Components:**
     - **Nodes:** Individual machines in the distributed system.
     - **Network:** The communication layer that connects nodes.
     - **Data Storage:** Distributed databases store data across multiple nodes.
     - **Coordination Services:** Manage coordination between nodes, ensuring consistency and handling failures.

2. **Data Distribution:**
   - **Sharding:**
     - Dividing a dataset into smaller, more manageable pieces called shards, which are distributed across multiple nodes.
     - Improves performance and scalability by parallelizing operations.
   - **Replication:**
     - Storing copies of data on multiple nodes to ensure high availability and fault tolerance.
     - Types of replication: Synchronous (all copies are updated simultaneously) and Asynchronous (copies are updated after the primary copy).

3. **Consistency Models:**
   - **Strong Consistency:**
     - Ensures that all nodes see the same data at the same time.
     - Achieved through techniques like distributed transactions and consensus algorithms.
   - **Eventual Consistency:**
     - Ensures that, given enough time, all nodes will eventually converge to the same state.
     - Suitable for systems where availability is more critical than immediate consistency.
   - **Causal Consistency:**
     - Ensures that causally related operations are seen by all nodes in the same order.

4. **Consensus Algorithms:**
   - **Paxos:**
     - A family of protocols for achieving consensus in a network of unreliable processors.
     - Ensures that a single value is agreed upon, even in the presence of failures.
   - **Raft:**
     - Designed to be more understandable than Paxos.
     - Divides the consensus problem into leader election, log replication, and safety.
   - **Zab (Zookeeper Atomic Broadcast):**
     - Used by Zookeeper to provide a high-performance coordination service for distributed applications.

5. **Fault Tolerance:**
   - **Redundancy:**
     - Storing multiple copies of data to protect against data loss.
   - **Failure Detection:**
     - Mechanisms to detect node failures and initiate recovery procedures.
   - **Failover:**
     - Automatically switching to a standby system or component upon the failure of the primary system.

6. **Coordination and Synchronization:**
   - **Leader Election:**
     - Process of designating a single node as the leader to coordinate actions among other nodes.
     - Ensures a single point of control for operations requiring strong consistency.
   - **Distributed Locks:**
     - Mechanisms to ensure that only one node can access a resource at a time.
     - Prevents conflicts and ensures data integrity.

7. **Communication in Distributed Systems:**
   - **Remote Procedure Calls (RPCs):**
     - Allows a program to cause a procedure to execute on a different address space (commonly on another physical machine).
   - **Message Passing:**
     - Nodes communicate by sending and receiving messages.
     - Asynchronous communication that can be implemented using various messaging protocols.

### Practical Examples

1. **Sharding Example:**
   - **Concept:** Dividing a user database into shards based on user ID.
   - **Example:**
     ```java
     public class ShardingExample {
         private Map<Integer, Database> shardMap = new HashMap<>();

         public ShardingExample() {
             shardMap.put(0, new Database("shard0"));
             shardMap.put(1, new Database("shard1"));
         }

         public Database getShard(int userId) {
             int shardId = userId % shardMap.size();
             return shardMap.get(shardId);
         }

         public static void main(String[] args) {
             ShardingExample shardingExample = new ShardingExample();
             Database shard = shardingExample.getShard(123);
             shard.insertUser(123, "John Doe");
         }
     }

     class Database {
         private String name;

         public Database(String name) {
             this.name = name;
         }

         public void insertUser(int userId, String userName) {
             // Insert user into database
             System.out.println("Inserting user " + userName + " into " + name);
         }
     }
     ```

2. **Leader Election Example (Zookeeper):**
   - **Concept:** Using Zookeeper for leader election in a distributed system.
   - **Example:**
     ```java
     import org.apache.zookeeper.*;

     public class LeaderElection implements Watcher {
         private ZooKeeper zooKeeper;
         private String electionNode = "/election";
         private String nodeId;

         public LeaderElection(String connectString) throws Exception {
             zooKeeper = new ZooKeeper(connectString, 3000, this);
             nodeId = zooKeeper.create(electionNode + "/n_", new byte[0], ZooDefs.Ids.OPEN_ACL_UNSAFE, CreateMode.EPHEMERAL_SEQUENTIAL);
             attemptLeadership();
         }

         private void attemptLeadership() throws Exception {
             List<String> nodes = zooKeeper.getChildren(electionNode, false);
             Collections.sort(nodes);
             if (nodeId.endsWith(nodes.get(0))) {
                 System.out.println("I am the leader");
             } else {
                 System.out.println("I am not the leader");
                 zooKeeper.exists(electionNode + "/" + nodes.get(0), this);
             }
         }

         @Override
         public void process(WatchedEvent event) {
             if (event.getType() == Event.EventType.NodeDeleted) {
                 try {
                     attemptLeadership();
                 } catch (Exception e) {
                     e.printStackTrace();
                 }
             }
         }

         public static void main(String[] args) throws Exception {
             new LeaderElection("localhost:2181");
         }
     }
     ```

3. **Consensus Algorithm (Raft) Example:**
   - **Concept:** Simplified implementation of Raft consensus algorithm for log replication.
   - **Example:**
     ```java
     import java.util.*;

     class RaftNode {
         private int nodeId;
         private int currentTerm;
         private int votedFor;
         private List<LogEntry> log;
         private int commitIndex;
         private int lastApplied;
         private Map<Integer, Integer> nextIndex;
         private Map<Integer, Integer> matchIndex;

         public RaftNode(int nodeId) {
             this.nodeId = nodeId;
             this.currentTerm = 0;
             this.votedFor = -1;
             this.log = new ArrayList<>();
             this.commitIndex = 0;
             this.lastApplied = 0;
             this.nextIndex = new HashMap<>();
             this.matchIndex = new HashMap<>();
         }

         public void requestVote(int term, int candidateId) {
             if (term > currentTerm) {
                 currentTerm = term;
                 votedFor = candidateId;
                 System.out.println("Node " + nodeId + " voted for " + candidateId);
             }
         }

         public void appendEntries(int term, int leaderId, List<LogEntry> entries, int leaderCommit) {
             if (term >= currentTerm) {
                 currentTerm = term;
                 log.addAll(entries);
                 if (leaderCommit > commitIndex) {
                     commitIndex = Math.min(leaderCommit, log.size() - 1);
                 }
                 System.out.println("Node " + nodeId + " appended entries from leader " + leaderId);
             }
         }
     }

     class LogEntry {
         int term;
         String command;

         public LogEntry(int term, String command) {
             this.term = term;
             this.command = command;
         }
     }

     public class RaftExample {
         public static void main(String[] args) {
             RaftNode node1 = new RaftNode(1);
             RaftNode node2 = new RaftNode(2);
             RaftNode node3 = new RaftNode(3);

             node1.requestVote(1, 1);
             node2.requestVote(1, 1);
             node3.requestVote(1, 1);

             List<LogEntry> entries = Arrays.asList(new LogEntry(1, "command1"), new LogEntry(1, "command2"));
             node1.appendEntries(1, 1, entries, 1);
             node2.appendEntries(1, 1, entries, 1);
             node3.appendEntries(1, 1, entries, 1);
         }
     }
     ```

### Key Points to Remember

- **Distributed Systems:** Enable databases to scale horizontally, providing high availability and fault tolerance.
- **Data Distribution:** Sharding and replication are key techniques for distributing data across multiple nodes.
- **Consistency Models:** Strong consistency, eventual consistency, and causal consistency address different requirements for data accuracy and availability.
- **Consensus Algorithms:** Paxos, Raft, and Zab ensure agreement among distributed nodes, essential for consistency and coordination.
- **Fault Tolerance:** Redundancy, failure detection, and failover mechanisms maintain system reliability.
- **Coordination Services:** Leader election and distributed locks ensure proper coordination and synchronization among nodes.

### Summary

- **Distributed Systems:** Essential for modern databases to achieve scalability, high availability, and fault tolerance.
- **Data Distribution and Coordination:** Key techniques and mechanisms to manage data across multiple nodes and ensure consistent and reliable operations.
- **Consensus and Fault Tolerance:** Fundamental for maintaining consistency and handling failures in distributed environments.

These detailed notes provide an overview and breakdown of the key concepts and examples from Chapter 8 of "Database Internals: A Deep Dive into How Distributed Data Systems Work" by Alex Petrov. For more in-depth explanations and additional exercises, refer to the full text of the book.