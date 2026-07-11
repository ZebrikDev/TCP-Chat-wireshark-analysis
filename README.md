# TCP Chat and Wireshark Traffic Analysis

A data communication project that demonstrates TCP/IP traffic analysis with Wireshark and a simple TCP chat application built with Python sockets.

---

## Project Overview

This project was built as part of a Data Communication / Computer Networks course.

The project includes two main parts:

1. HTTP traffic analysis using a CSV file, Jupyter Notebook, and Wireshark.
2. TCP chat application using Python sockets and threads.

---

## Technologies Used

- Python
- TCP/IP
- Socket Programming
- Threading
- Jupyter Notebook
- Wireshark
- CSV

---

## Skills Demonstrated

- Client-Server Architecture
- TCP Socket Programming
- Multi-threaded Programming
- Network Traffic Analysis
- HTTP Protocol Analysis
- Wireshark Packet Inspection
- TCP/IP Communication
- Data Encapsulation

---

## Part 1: HTTP Traffic Analysis

In the first part, the project uses a CSV file that contains HTTP messages at the application layer.

Example CSV row:

```csv
1,HTTP,client_browser,web_server,GET /index.html,0.015
```

Each row describes one application-layer message, including:

- message ID
- application protocol
- source application
- destination application
- message content
- timestamp

The Jupyter Notebook loads the CSV file, simulates TCP/IP encapsulation, and creates real HTTP traffic that can be captured in Wireshark.

### Main files

- `data_input_main.csv`
- `traffic_demo_http.ipynb`

### Wireshark filter for this part

```text
tcp.port == 8080
```

The HTTP demo runs locally on:

```text
127.0.0.1:8080
```

This means that the client and server in the Jupyter demonstration run on the same computer using localhost / loopback.

---

## Part 2: TCP Chat Application

The second part is a simple chat system implemented in Python.

The application contains two main files:

- `server.py`
- `client.py`

The server listens for incoming TCP connections and routes messages between connected clients.

Each client connects to the server, sends a unique username, and can send messages to another connected client using this format:

```text
TargetName:Message
```

Example:

```text
Bob:Hello Bob
```

The server receives the message, finds the target client by name, and forwards the message to the correct socket.

---

## Technologies Used

- Python
- TCP sockets
- Threading
- Wireshark
- Jupyter Notebook
- CSV

Only built-in Python libraries are used for the chat application:

```python
import socket
import threading
```

No external server/client frameworks are used.

---

## How to Run the Chat Application

### 1. Run the server

On the server computer, run:

```bash
python3 server.py
```

The server listens on:

```text
0.0.0.0:50001
```

`0.0.0.0` means that the server listens on all network interfaces of the computer.

### 2. Run a client

On the client computer, run:

```bash
python3 client.py
```

If the client runs on another computer in the same Wi-Fi network, replace the host value in `client.py` with the local IP address of the server computer.

Example:

```python
HOST = "SERVER_IP_HERE"
PORT = 50001
```

### 3. Run multiple clients

To test several clients, open multiple terminal windows and run `client.py` in each one.

Example usernames:

```text
Alice
Bob
Charlie
David
Eve
```

---

## Wireshark Analysis

### HTTP traffic from Jupyter

Use this display filter:

```text
tcp.port == 8080
```

In this capture, Wireshark can show:

- TCP three-way handshake
- HTTP GET requests
- HTTP `200 OK` responses
- TCP acknowledgments
- TCP connection closing

### Chat application traffic

Use this display filter:

```text
tcp.port == 50001
```

In this capture:

- The server uses the fixed port `50001`.
- The clients use temporary ports assigned by the operating system.
- TCP connections start with a three-way handshake.
- Packets with `PSH, ACK` and `Len > 0` usually contain real application data, such as usernames or chat messages.

Example TCP handshake:

```text
Client → Server: SYN
Server → Client: SYN, ACK
Client → Server: ACK
```

---

## Key Networking Concepts

### Socket

A socket is a communication endpoint used by an application to send and receive data over the network.

In this project, sockets are used to create TCP communication between the client and the server.

### TCP

TCP is a reliable transport-layer protocol. It establishes a connection, keeps data in order, and uses acknowledgments to confirm that data was received.

### Thread

A thread allows a program to perform multiple tasks at the same time.

In this project:

- The server uses a separate thread for each connected client.
- The client uses a background thread to receive messages while the user can still type.

### Three-Way Handshake

TCP opens a connection using three steps:

```text
SYN → SYN, ACK → ACK
```

After this process, the TCP connection is established.

### PSH, ACK

`PSH, ACK` usually means that real application data is being sent and that previous data is acknowledged.

### Len

`Len` shows the amount of TCP payload data.

- `Len = 0` usually means TCP control traffic only.
- `Len > 0` means that real data is being transferred.

---

## What I Learned

Through this project, I practiced and learned:

- how TCP client-server communication works
- how sockets are used in Python
- how threads allow multiple clients to work at the same time
- how to capture TCP/IP traffic using Wireshark
- how to identify TCP handshakes, acknowledgments, ports, and payload data
- how application-layer messages are encapsulated inside TCP and IP

---

## License

This project is intended for educational purposes and can be published with the MIT License.
