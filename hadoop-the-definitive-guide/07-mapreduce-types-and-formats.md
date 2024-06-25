 ### Detailed Notes on Chapter 7: MapReduce Types and Formats
**"Hadoop: The Definitive Guide" by Tom White**

#### **Overview**
Chapter 7 explores the various types and formats used in Hadoop MapReduce, focusing on input and output types, custom data types, and the mechanisms for reading and writing different data formats. Understanding these concepts is crucial for developing efficient MapReduce applications that handle diverse data sources and outputs.

#### **Key Sections and Points**

1. **MapReduce Types**
   - **Key-Value Pair Types**:
     - MapReduce operates on key-value pairs.
     - The types of keys and values are specified by the `Mapper` and `Reducer` classes.
     - Example:
       ```java
       public class MyMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
           // Mapper implementation
       }
       public class MyReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
           // Reducer implementation
       }
       ```
   - **Writable Interface**:
     - Hadoop uses the `Writable` interface for serialization.
     - Common `Writable` types: `IntWritable`, `LongWritable`, `Text`, `NullWritable`.
   - **WritableComparable Interface**:
     - Extends `Writable` and `Comparable` interfaces.
     - Used for keys in MapReduce jobs to ensure they can be compared and sorted.

2. **Input Formats**
   - **InputFormat Class**:
     - Determines how input files are split and read.
     - Defines the `InputSplit` and `RecordReader` classes.
   - **Common Input Formats**:
     - **TextInputFormat**: Default format, reads lines of text files.
     - **KeyValueTextInputFormat**: Parses input into key-value pairs separated by a tab.
     - **SequenceFileInputFormat**: Reads binary sequence files.
     - **NLineInputFormat**: Splits input at fixed number of lines per split.
   - **Custom Input Formats**:
     - Creating custom input formats by extending `FileInputFormat` and implementing `RecordReader`.

3. **Output Formats**
   - **OutputFormat Class**:
     - Determines how output files are written.
     - Defines the `RecordWriter` class.
   - **Common Output Formats**:
     - **TextOutputFormat**: Default format, writes key-value pairs as text.
     - **SequenceFileOutputFormat**: Writes binary sequence files.
     - **MapFileOutputFormat**: Writes output as a sorted `MapFile`.
   - **Custom Output Formats**:
     - Creating custom output formats by extending `FileOutputFormat` and implementing `RecordWriter`.

4. **Implementing a Custom Writable**
   - **Custom Writable Class**:
     - Implementing `Writable` interface methods `write(DataOutput out)` and `readFields(DataInput in)`.
     - Example:
       ```java
       public class MyWritable implements Writable {
           private int counter;
           private long timestamp;

           public void write(DataOutput out) throws IOException {
               out.writeInt(counter);
               out.writeLong(timestamp);
           }

           public void readFields(DataInput in) throws IOException {
               counter = in.readInt();
               timestamp = in.readLong();
           }
       }
       ```

5. **Input and Output Format Examples**
   - **Reading and Writing Text Files**:
     - Using `TextInputFormat` and `TextOutputFormat`.
     - Example:
       ```java
       job.setInputFormatClass(TextInputFormat.class);
       job.setOutputFormatClass(TextOutputFormat.class);
       ```
   - **Reading and Writing Sequence Files**:
     - Using `SequenceFileInputFormat` and `SequenceFileOutputFormat`.
     - Example:
       ```java
       job.setInputFormatClass(SequenceFileInputFormat.class);
       job.setOutputFormatClass(SequenceFileOutputFormat.class);
       ```

6. **Data Compression**
   - **Compression Codecs**:
     - Hadoop supports various compression codecs: Gzip, Bzip2, LZO, Snappy.
   - **Compressing Map Output**:
     - Setting the compression codec for map output:
       ```java
       conf.set("mapreduce.map.output.compress", "true");
       conf.set("mapreduce.map.output.compress.codec", "org.apache.hadoop.io.compress.SnappyCodec");
       ```
   - **Compressing Job Output**:
     - Setting the compression codec for job output:
       ```java
       FileOutputFormat.setCompressOutput(job, true);
       FileOutputFormat.setOutputCompressorClass(job, GzipCodec.class);
       ```

7. **Multiple Outputs**
   - **MultipleOutputs Class**:
     - Allows writing to multiple output files from a single MapReduce job.
     - Example:
       ```java
       MultipleOutputs.addNamedOutput(job, "text", TextOutputFormat.class, Text.class, IntWritable.class);
       ```
   - **Writing to Named Outputs**:
     - Example:
       ```java
       MultipleOutputs<Text, IntWritable> mos = new MultipleOutputs<>(context);
       mos.write("text", key, value, "text/part");
       ```

8. **Reading and Writing Data with Avro**
   - **Avro Data Files**:
     - Avro provides a compact, fast, binary data format.
   - **AvroInputFormat and AvroOutputFormat**:
     - Using Avro input and output formats in MapReduce jobs.
     - Example:
       ```java
       job.setInputFormatClass(AvroKeyInputFormat.class);
       job.setOutputFormatClass(AvroKeyOutputFormat.class);
       ```

### **Summary**
Chapter 7 of "Hadoop: The Definitive Guide" provides an in-depth understanding of the types and formats used in Hadoop MapReduce. It covers the key-value pair types, the `Writable` and `WritableComparable` interfaces, and how to implement custom writables. The chapter explains common input and output formats, how to create custom formats, and how to handle data compression in MapReduce jobs. It also introduces the `MultipleOutputs` class for writing to multiple output files and explains how to work with Avro data files. This knowledge is crucial for developing flexible and efficient MapReduce applications that can handle diverse data sources and outputs effectively.