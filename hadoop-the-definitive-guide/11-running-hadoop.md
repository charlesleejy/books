### Detailed Notes on Chapter 11: Running Hadoop
**"Hadoop: The Definitive Guide" by Tom White**

#### **Overview**
Chapter 11 focuses on the operational aspects of running Hadoop, covering the command-line interface, administration through scripts, and Hadoop streaming and pipes. These tools and techniques are essential for effectively managing and utilizing a Hadoop cluster.

#### **Key Sections and Points**

1. **The Command-Line Interface**
   - **Hadoop Shell Commands**:
     - Hadoop provides a set of shell commands for interacting with HDFS.
   - **Basic Commands**:
     - Listing files:
       ```sh
       hdfs dfs -ls /path
       ```
     - Creating directories:
       ```sh
       hdfs dfs -mkdir /path
       ```
     - Uploading files:
       ```sh
       hdfs dfs -put localfile /path
       ```
     - Downloading files:
       ```sh
       hdfs dfs -get /path localfile
       ```
     - Deleting files and directories:
       ```sh
       hdfs dfs -rm /path
       hdfs dfs -rmdir /path
       ```
   - **Advanced Commands**:
     - Checking file integrity:
       ```sh
       hdfs dfs -checksum /path
       ```
     - Changing file permissions:
       ```sh
       hdfs dfs -chmod 755 /path
       ```
     - Changing file ownership:
       ```sh
       hdfs dfs -chown user:group /path
       ```

2. **Hadoop Administration Commands**
   - **Administrative Tools**:
     - Commands to manage and monitor the Hadoop cluster.
   - **Starting and Stopping Services**:
     - Starting HDFS:
       ```sh
       start-dfs.sh
       ```
     - Stopping HDFS:
       ```sh
       stop-dfs.sh
       ```
     - Starting YARN:
       ```sh
       start-yarn.sh
       ```
     - Stopping YARN:
       ```sh
       stop-yarn.sh
       ```
   - **Cluster Health and Maintenance**:
     - Checking HDFS health:
       ```sh
       hdfs dfsadmin -report
       ```
     - Balancing HDFS data:
       ```sh
       hdfs balancer
       ```
     - Decommissioning a node:
       ```sh
       hdfs dfsadmin -decommission datanode
       ```
   - **File System Checking (fsck)**:
     - Running fsck to check for inconsistencies in HDFS:
       ```sh
       hdfs fsck /
       ```

3. **Hadoop Streaming**
   - **Introduction**:
     - Hadoop Streaming allows writing MapReduce jobs in any language that can read from standard input and write to standard output.
   - **Writing a Streaming Job**:
     - Example Python Mapper:
       ```python
       import sys
       for line in sys.stdin:
           print(line.strip())
       ```
     - Example Python Reducer:
       ```python
       import sys
       from collections import defaultdict

       counts = defaultdict(int)
       for line in sys.stdin:
           word, count = line.strip().split()
           counts[word] += int(count)
       for word, count in counts.items():
           print(f"{word}\t{count}")
       ```
   - **Running a Streaming Job**:
     - Submitting the job:
       ```sh
       hadoop jar /path/to/hadoop-streaming.jar \
           -input /input/path \
           -output /output/path \
           -mapper /path/to/mapper.py \
           -reducer /path/to/reducer.py
       ```

4. **Hadoop Pipes**
   - **Introduction**:
     - Hadoop Pipes is an interface for writing MapReduce programs in C++.
   - **Writing a Pipes Job**:
     - Example C++ Mapper:
       ```cpp
       #include <iostream>
       #include <mapreduce/mapreduce.h>

       class WordCountMapper : public HadoopPipes::Mapper {
       public:
           WordCountMapper(HadoopPipes::TaskContext& context) {}

           void map(HadoopPipes::MapContext& context) {
               std::string line = context.getInputValue();
               std::istringstream stream(line);
               std::string word;
               while (stream >> word) {
                   context.emit(word, "1");
               }
           }
       };
       ```
     - Example C++ Reducer:
       ```cpp
       #include <iostream>
       #include <mapreduce/mapreduce.h>

       class WordCountReducer : public HadoopPipes::Reducer {
       public:
           WordCountReducer(HadoopPipes::TaskContext& context) {}

           void reduce(HadoopPipes::ReduceContext& context) {
               int count = 0;
               while (context.nextValue()) {
                   count += std::stoi(context.getInputValue());
               }
               context.emit(context.getInputKey(), std::to_string(count));
           }
       };
       ```
   - **Running a Pipes Job**:
     - Submitting the job:
       ```sh
       hadoop pipes \
           -input /input/path \
           -output /output/path \
           -program /path/to/pipes-program \
           -reduces 1
       ```

5. **Distributed Cache**
   - **Purpose**:
     - The distributed cache mechanism allows MapReduce jobs to access read-only files needed by tasks.
   - **Using the Distributed Cache**:
     - Adding files to the distributed cache:
       ```java
       job.addCacheFile(new URI("/path/to/cache/file#alias"));
       ```
     - Accessing cached files in the job:
       ```java
       Path[] cacheFiles = context.getLocalCacheFiles();
       ```

6. **Job Scheduling**
   - **FIFO Scheduler**:
     - The default job scheduler in Hadoop.
   - **Fair Scheduler**:
     - Allocates resources to jobs such that all jobs get, on average, an equal share of resources over time.
   - **Capacity Scheduler**:
     - Allows for the sharing of large clusters while giving each organization a minimum capacity guarantee.

7. **Debugging MapReduce Jobs**
   - **Local Debugging**:
     - Running jobs locally for debugging purposes.
     - Example:
       ```java
       conf.set("mapreduce.framework.name", "local");
       ```
   - **Logging**:
     - Accessing logs to troubleshoot job execution issues:
       ```sh
       hadoop job -logs job_id
       ```
   - **Web UI**:
     - Using the Hadoop Web UI to monitor and debug running jobs.

### **Summary**
Chapter 11 of "Hadoop: The Definitive Guide" provides a detailed guide to running Hadoop, focusing on the command-line interface, administrative tools, and advanced features like Hadoop Streaming and Hadoop Pipes. It covers essential shell commands for interacting with HDFS, starting and stopping Hadoop services, and maintaining cluster health. The chapter also introduces Hadoop Streaming and Pipes, allowing users to write MapReduce jobs in languages other than Java. Additionally, it covers the distributed cache mechanism for sharing read-only data and job scheduling strategies for managing cluster resources. Finally, it discusses debugging techniques for troubleshooting MapReduce jobs, ensuring efficient and effective Hadoop cluster management.