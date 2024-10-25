# Distributed Peer-to-Peer Application

This project implements a simple distributed peer-to-peer (P2P) application using Python's `asyncio` library. The application consists of two nodes that communicate with each other to send and process instructions.

## Overview

The application demonstrates how to create asynchronous network servers and clients using `asyncio`. Each node listens for incoming connections, processes received instructions, and sends responses. The project is structured into two main components: `PeerNode 1` and `PeerNode 2`, each capable of sending and receiving specific types of instructions.

## Features

- Asynchronous handling of multiple client connections.
- Simple instruction processing and response mechanism.
- Node discovery and connection establishment.
- File-based instruction reading for dynamic input.

## Architecture

### PeerNode Class

The `PeerNode` class contains several key methods that enable the functionality of the nodes:

1. **`__init__(self, host='localhost', port=8888)`**: Initializes an instance of the `PeerNode` class, setting up the host and port attributes, along with lists for instructions and connections.

2. **`async def handle_client(self, reader, writer)`**: Manages incoming client connections by continuously reading data from connected clients. It processes the received messages and sends back appropriate responses.

3. **`async def run_server(self)`**: Sets up the server using `asyncio.start_server()` to listen for incoming connections. It links the `handle_client` method for handling each connection, allowing the server to run indefinitely.

4. **`async def read_instructions(self, file_path)`**: Reads instructions from a specified file. It filters and stores instructions based on their prefixes (e.g., 'a' or 'b') in the `self.instructions` attribute.

5. **`async def connect_to_nodes(self, nodes)`**: Connects to other nodes by accepting a list of node addresses. It opens connections and appends the corresponding `reader` and `writer` objects for communication.

6. **`async def send_instructions(self)`**: Sends the stored instructions to the connected nodes. It waits for responses from each node after sending the instructions, facilitating acknowledgment.

7. **`async def main(self)`**: Acts as the entry point for executing asynchronous operations. It starts the server, reads instructions, connects to other nodes, and sends instructions while managing the lifecycle of connections.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `asyncio` library (included in the standard library)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/NafTan1/SMC-Labs-Case-Study.git

### Running the Application

To run the application, open two windows and execute the following commands:

##### In Terminal 1 (for Node 1) 
  ```bash
   python pNode1.py
  ```

##### In Terminal 2 (for Node 1) 
  ```bash
   python pNode2.py
  ```



