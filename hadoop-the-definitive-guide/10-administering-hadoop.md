### Detailed Notes on Chapter 10: Administering Hadoop
**"Hadoop: The Definitive Guide" by Tom White**

#### **Overview**
Chapter 10 focuses on the administrative tasks necessary for managing a Hadoop cluster. It covers various aspects such as monitoring, maintenance, metadata management, data integrity, and security. Understanding these tasks is crucial for ensuring the smooth operation and efficiency of a Hadoop cluster.

#### **Key Sections and Points**

1. **HDFS**
   - **NameNode and DataNode Management**:
     - NameNode: Manages the filesystem namespace and metadata.
     - DataNodes: Store the actual data and report to the NameNode periodically.
   - **Starting and Stopping HDFS**:
     - Commands to start and stop HDFS services:
       ```sh
       start-dfs.sh
       stop-dfs.sh
       ```
   - **Safe Mode**:
     - Safe mode is a read-only mode for HDFS to ensure data integrity during startup or maintenance.
     - Entering and leaving safe mode:
       ```sh
       hdfs dfsadmin -safemode enter
       hdfs dfsadmin -safemode leave
       ```

2. **Monitoring**
   - **Hadoop Metrics**:
     - Monitoring critical Hadoop metrics using tools like Ganglia, Nagios, or the Hadoop built-in UI.
   - **HDFS Web UI**:
     - Accessing the HDFS web interface to monitor NameNode and DataNode status:
       ```sh
       http://namenode-host:9870
       ```
   - **YARN Web UI**:
     - Monitoring YARN ResourceManager and NodeManager status:
       ```sh
       http://resourcemanager-host:8088
       ```

3. **Maintenance**
   - **Balancing HDFS Data**:
     - Using the HDFS balancer to distribute data evenly across DataNodes:
       ```sh
       hdfs balancer
       ```
   - **Decommissioning Nodes**:
     - Safely removing nodes from the cluster by decommissioning them:
       ```sh
       hdfs dfsadmin -refreshNodes
       ```
   - **Upgrading Hadoop**:
     - Steps to upgrade Hadoop with minimal downtime.
   - **Filesystem Checking**:
     - Using `fsck` to check the health of HDFS:
       ```sh
       hdfs fsck /
       ```

4. **Metadata and the Checkpoint**
   - **Checkpointing**:
     - Periodically saving the NameNode’s in-memory metadata to persistent storage.
   - **Secondary NameNode**:
     - Role of the Secondary NameNode in checkpointing.
     - Commands to start and stop the Secondary NameNode:
       ```sh
       start-sec-secondary.sh
       stop-sec-secondary.sh
       ```

5. **Data Integrity**
   - **Checksum Verification**:
     - HDFS uses checksums to ensure data integrity.
   - **Data Corruption**:
     - Detecting and handling data corruption:
       ```sh
       hdfs fsck /
       ```

6. **Backup and Recovery**
   - **Backup Strategies**:
     - Regularly backing up critical data and metadata.
   - **Data Recovery**:
     - Using HDFS snapshots for point-in-time recovery.

7. **Managing HDFS Quotas**
   - **Space Quotas**:
     - Limiting the amount of disk space used by a directory:
       ```sh
       hdfs dfsadmin -setSpaceQuota 10G /path/to/dir
       hdfs dfsadmin -clrSpaceQuota /path/to/dir
       ```
   - **Namespace Quotas**:
     - Limiting the number of files and directories in a directory:
       ```sh
       hdfs dfsadmin -setQuota 1000 /path/to/dir
       hdfs dfsadmin -clrQuota /path/to/dir
       ```

8. **User Management**
   - **Managing Permissions**:
     - Setting file and directory permissions using Unix-style permission bits.
     - Example:
       ```sh
       hdfs dfs -chmod 755 /path/to/dir
       hdfs dfs -chown user:group /path/to/dir
       hdfs dfs -chgrp group /path/to/dir
       ```

9. **Security**
   - **Kerberos Authentication**:
     - Enabling Kerberos for secure authentication.
     - Configuring Kerberos principals and keytabs.
   - **HDFS Encryption**:
     - Encrypting data at rest and in transit.
     - Configuring Transparent Data Encryption (TDE) in HDFS.

10. **High Availability**
    - **NameNode HA**:
      - Configuring NameNode high availability with automatic failover.
      - Using JournalNode or shared storage for metadata synchronization.
    - **ResourceManager HA**:
      - Enabling ResourceManager high availability for fault tolerance.

11. **YARN Administration**
    - **Resource Management**:
      - Configuring resource allocation and scheduling policies.
      - Using the Fair Scheduler or Capacity Scheduler.
    - **Monitoring Applications**:
      - Tracking application status and logs through the YARN web UI.

### **Summary**
Chapter 10 of "Hadoop: The Definitive Guide" provides a detailed guide to administering a Hadoop cluster. It covers essential tasks such as starting and stopping HDFS, monitoring the cluster, performing maintenance activities like balancing data and decommissioning nodes, and managing metadata through checkpointing. The chapter also discusses data integrity mechanisms, backup and recovery strategies, managing HDFS quotas, and user management. Additionally, it covers security aspects including Kerberos authentication and HDFS encryption, and ensures high availability for both NameNode and ResourceManager. This comprehensive coverage equips administrators with the knowledge needed to maintain a stable, secure, and efficient Hadoop cluster.