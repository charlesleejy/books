## Chapter 18: Distributed Computing: RMI and Networking

#### Overview
- This chapter explores the concepts of distributed computing using Java RMI (Remote Method Invocation) and networking.
- It explains how to create and deploy distributed applications that can interact over a network.

### Key Concepts

1. **Distributed Computing**
   - **Definition:** Computing processes spread across multiple networked computers to improve efficiency and performance.
   - **Purpose:** Enables resource sharing, load balancing, and parallel processing.

2. **Remote Method Invocation (RMI)**
   - **Definition:** A Java API that allows methods to be invoked from an object running in another Java Virtual Machine.
   - **Components:**
     - **Remote Interface:** Defines the methods that can be called remotely.
     - **Remote Object:** Implements the remote interface and provides the functionality of the remote methods.
     - **RMI Registry:** A simple name service that allows clients to obtain a reference to a remote object.

3. **Networking Basics**
   - **Sockets:** Endpoints for communication between two machines over a network.
   - **Client-Server Model:** A network architecture where clients request services and servers provide them.

### Detailed Breakdown

1. **Remote Interface**
   - **Definition:** An interface that declares the methods that can be called remotely.
   - **Example:**
     ```java
     import java.rmi.Remote;
     import java.rmi.RemoteException;

     public interface MyRemote extends Remote {
         String sayHello() throws RemoteException;
     }
     ```

2. **Remote Object Implementation**
   - **Definition:** A class that implements the remote interface and provides the actual method implementations.
   - **Example:**
     ```java
     import java.rmi.server.UnicastRemoteObject;
     import java.rmi.RemoteException;

     public class MyRemoteImpl extends UnicastRemoteObject implements MyRemote {
         public MyRemoteImpl() throws RemoteException {
             super();
         }

         public String sayHello() throws RemoteException {
             return "Hello, RMI!";
         }
     }
     ```

3. **Setting Up the RMI Server**
   - **Steps:**
     1. Create and export a remote object.
     2. Bind the remote object to the RMI registry.
   - **Example:**
     ```java
     import java.rmi.registry.LocateRegistry;
     import java.rmi.registry.Registry;

     public class MyRemoteServer {
         public static void main(String[] args) {
             try {
                 MyRemote service = new MyRemoteImpl();
                 Registry registry = LocateRegistry.createRegistry(1099);
                 registry.rebind("RemoteHello", service);
                 System.out.println("Service bound and ready");
             } catch (Exception e) {
                 e.printStackTrace();
             }
         }
     }
     ```

4. **Creating the RMI Client**
   - **Steps:**
     1. Lookup the remote object in the RMI registry.
     2. Call the remote method.
   - **Example:**
     ```java
     import java.rmi.registry.LocateRegistry;
     import java.rmi.registry.Registry;

     public class MyRemoteClient {
         public static void main(String[] args) {
             try {
                 Registry registry = LocateRegistry.getRegistry("localhost");
                 MyRemote service = (MyRemote) registry.lookup("RemoteHello");
                 String response = service.sayHello();
                 System.out.println("Response: " + response);
             } catch (Exception e) {
                 e.printStackTrace();
             }
         }
     }
     ```

5. **Networking with Sockets**
   - **Client-Server Communication:**
     - **Server:** Listens for client connections.
     - **Client:** Connects to the server and exchanges data.
   - **Example:**
     ```java
     // Server
     import java.io.*;
     import java.net.*;

     public class SimpleServer {
         public static void main(String[] args) {
             try (ServerSocket serverSocket = new ServerSocket(12345)) {
                 System.out.println("Server is listening on port 12345");
                 Socket socket = serverSocket.accept();
                 BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                 String message = in.readLine();
                 System.out.println("Received: " + message);
                 out.println("Hello, Client!");
                 socket.close();
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }

     // Client
     import java.io.*;
     import java.net.*;

     public class SimpleClient {
         public static void main(String[] args) {
             try (Socket socket = new Socket("localhost", 12345)) {
                 PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                 BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 out.println("Hello, Server!");
                 String response = in.readLine();
                 System.out.println("Response: " + response);
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }
     ```

### Practical Examples

1. **RMI Chat Application**
   - **Remote Interface:**
     ```java
     import java.rmi.Remote;
     import java.rmi.RemoteException;

     public interface ChatService extends Remote {
         void sendMessage(String message) throws RemoteException;
         String receiveMessage() throws RemoteException;
     }
     ```
   - **Remote Object Implementation:**
     ```java
     import java.rmi.server.UnicastRemoteObject;
     import java.rmi.RemoteException;
     import java.util.LinkedList;
     import java.util.Queue;

     public class ChatServiceImpl extends UnicastRemoteObject implements ChatService {
         private Queue<String> messages = new LinkedList<>();

         public ChatServiceImpl() throws RemoteException {
             super();
         }

         public synchronized void sendMessage(String message) throws RemoteException {
             messages.add(message);
         }

         public synchronized String receiveMessage() throws RemoteException {
             return messages.poll();
         }
     }
     ```
   - **Server:**
     ```java
     import java.rmi.registry.LocateRegistry;
     import java.rmi.registry.Registry;

     public class ChatServer {
         public static void main(String[] args) {
             try {
                 ChatService service = new ChatServiceImpl();
                 Registry registry = LocateRegistry.createRegistry(1099);
                 registry.rebind("ChatService", service);
                 System.out.println("Chat service bound and ready");
             } catch (Exception e) {
                 e.printStackTrace();
             }
         }
     }
     ```
   - **Client:**
     ```java
     import java.rmi.registry.LocateRegistry;
     import java.rmi.registry.Registry;
     import java.util.Scanner;

     public class ChatClient {
         public static void main(String[] args) {
             try {
                 Registry registry = LocateRegistry.getRegistry("localhost");
                 ChatService service = (ChatService) registry.lookup("ChatService");
                 Scanner scanner = new Scanner(System.in);
                 
                 Thread receiverThread = new Thread(() -> {
                     while (true) {
                         try {
                             String message = service.receiveMessage();
                             if (message != null) {
                                 System.out.println("Received: " + message);
                             }
                         } catch (RemoteException e) {
                             e.printStackTrace();
                         }
                     }
                 });
                 receiverThread.start();

                 while (true) {
                     String message = scanner.nextLine();
                     service.sendMessage(message);
                 }
             } catch (Exception e) {
                 e.printStackTrace();
             }
         }
     }
     ```

2. **Multi-Threaded Networking Server**
   - **Server:**
     ```java
     import java.io.*;
     import java.net.*;

     public class MultiThreadedServer {
         public static void main(String[] args) {
             try (ServerSocket serverSocket = new ServerSocket(12345)) {
                 System.out.println("Server is listening on port 12345");
                 while (true) {
                     Socket socket = serverSocket.accept();
                     new ClientHandler(socket).start();
                 }
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }

     class ClientHandler extends Thread {
         private Socket socket;

         public ClientHandler(Socket socket) {
             this.socket = socket;
         }

         public void run() {
             try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                  PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
                 String message;
                 while ((message = in.readLine()) != null) {
                     System.out.println("Received: " + message);
                     out.println("Echo: " + message);
                 }
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }
     ```
   - **Client:**
     ```java
     import java.io.*;
     import java.net.*;

     public class MultiThreadedClient {
         public static void main(String[] args) {
             try (Socket socket = new Socket("localhost", 12345);
                  PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                  BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                  BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))) {
                 String userInput;
                 while ((userInput = stdIn.readLine()) != null) {
                     out.println(userInput);
                     System.out.println("Echo: " + in.readLine());
                 }
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }
     ```

### Key Points to Remember

- **RMI (Remote Method Invocation):** Enables Java applications to invoke methods on remote objects, facilitating distributed computing.
- **Networking with Sockets:** Use sockets to create client-server applications for communication over a network.
- **Client-Server Model:** The server listens for client requests and the