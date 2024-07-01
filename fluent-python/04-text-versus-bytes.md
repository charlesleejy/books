## Chapter 4: Text versus Bytes

#### Overview
- This chapter explores the differences between text (str) and bytes (byte sequences) in Python.
- Understanding these differences is crucial for handling data correctly, especially when working with files, network communication, and various input/output operations.

### Key Concepts

1. **Text and Binary Data**
   - **Text (str):** Represents human-readable characters. In Python 3, text is always Unicode.
   - **Bytes (byte sequences):** Represents raw binary data, including text encoded in a specific format.

2. **Unicode and Encodings**
   - **Unicode:** A standard for representing text in different writing systems. Each character is assigned a unique code point.
   - **Encoding:** A way to convert Unicode code points to a sequence of bytes. Common encodings include UTF-8, UTF-16, and Latin-1.

3. **String and Byte Literals**
   - **String literals:** Enclosed in single, double, or triple quotes.
     ```python
     text = 'hello'
     ```
   - **Byte literals:** Prefixed with `b` or `B` and enclosed in single or double quotes.
     ```python
     data = b'hello'
     ```

### Encoding and Decoding

1. **Encoding Strings to Bytes**
   - **Method:** `str.encode(encoding)`
   - **Example:**
     ```python
     text = 'café'
     data = text.encode('utf-8')
     print(data)  # Output: b'caf\xc3\xa9'
     ```

2. **Decoding Bytes to Strings**
   - **Method:** `bytes.decode(encoding)`
   - **Example:**
     ```python
     data = b'caf\xc3\xa9'
     text = data.decode('utf-8')
     print(text)  # Output: café
     ```

### Byte Essentials

1. **Byte Sequences in Detail**
   - **Bytes Type:** Immutable sequences of bytes.
     ```python
     data = b'hello'
     ```
   - **Bytearray Type:** Mutable sequences of bytes.
     ```python
     data = bytearray(b'hello')
     data[0] = 72
     print(data)  # Output: bytearray(b'Hello')
     ```

2. **Bytes and Bytearray Methods**
   - **Common Methods:**
     - `data.split()`
     - `data.replace(b'old', b'new')`
   - **Example:**
     ```python
     data = b'hello world'
     print(data.split())  # Output: [b'hello', b'world']
     ```

### Basic Encoders/Decoders

1. **Working with Different Encodings**
   - **Example:**
     ```python
     text = 'café'
     data_utf8 = text.encode('utf-8')
     data_utf16 = text.encode('utf-16')
     print(data_utf8)  # Output: b'caf\xc3\xa9'
     print(data_utf16)  # Output: b'\xff\xfec\x00a\x00f\x00\xe9\x00'
     ```

2. **Handling Encoding Errors**
   - **Methods:** `errors='ignore'`, `errors='replace'`, `errors='backslashreplace'`
   - **Example:**
     ```python
     text = 'café'
     data = text.encode('ascii', errors='replace')
     print(data)  # Output: b'caf?'
     ```

### Reading and Writing Files

1. **Reading Text Files**
   - **Method:** `open(filename, mode, encoding)`
   - **Example:**
     ```python
     with open('example.txt', 'r', encoding='utf-8') as f:
         text = f.read()
     print(text)
     ```

2. **Writing Text Files**
   - **Method:** `open(filename, mode, encoding)`
   - **Example:**
     ```python
     text = 'café'
     with open('example.txt', 'w', encoding='utf-8') as f:
         f.write(text)
     ```

3. **Reading Binary Files**
   - **Method:** `open(filename, 'rb')`
   - **Example:**
     ```python
     with open('example.bin', 'rb') as f:
         data = f.read()
     print(data)
     ```

4. **Writing Binary Files**
   - **Method:** `open(filename, 'wb')`
   - **Example:**
     ```python
     data = b'café'
     with open('example.bin', 'wb') as f:
         f.write(data)
     ```

### Handling Text Files

1. **Reading Lines from a Text File**
   - **Example:**
     ```python
     with open('example.txt', 'r', encoding='utf-8') as f:
         for line in f:
             print(line.strip())
     ```

2. **Writing Lines to a Text File**
   - **Example:**
     ```python
     lines = ['first line', 'second line', 'third line']
     with open('example.txt', 'w', encoding='utf-8') as f:
         for line in lines:
             f.write(line + '\n')
     ```

### Practical Examples

1. **Reading and Writing JSON Files**
   - **Reading JSON:**
     ```python
     import json
     with open('data.json', 'r', encoding='utf-8') as f:
         data = json.load(f)
     print(data)
     ```
   - **Writing JSON:**
     ```python
     data = {'name': 'café', 'location': 'Paris'}
     with open('data.json', 'w', encoding='utf-8') as f:
         json.dump(data, f, ensure_ascii=False)
     ```

2. **Handling CSV Files**
   - **Reading CSV:**
     ```python
     import csv
     with open('data.csv', 'r', encoding='utf-8') as f:
         reader = csv.reader(f)
         for row in reader:
             print(row)
     ```
   - **Writing CSV:**
     ```python
     data = [['name', 'location'], ['café', 'Paris']]
     with open('data.csv', 'w', encoding='utf-8', newline='') as f:
         writer = csv.writer(f)
         writer.writerows(data)
     ```

### Conclusion
- Understanding the distinction between text (str) and bytes is fundamental for correctly handling data in Python.
- Proper encoding and decoding practices ensure that text data is correctly processed and transmitted.
- Python provides robust tools for working with both text and binary data, making it versatile for various applications, from file I/O to network communication.

These detailed notes cover the key concepts and examples from Chapter 4 of "Fluent Python" by Luciano Ramalho. For more in-depth explanations and practical examples, refer to the book directly.