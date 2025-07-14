# Simple Server-Client Chat Application

This is a basic command-line chat application built with Python's `socket` module, demonstrating a simple client-server communication model.

## Features

* **Real-time Messaging**: Exchange messages instantly between the server and a single client.
* **Command-Line Interface**: Interact with the chat through your terminal.
* **Basic Socket Communication**: Utilizes Python's built-in `socket` library for network communication.

## How it Works

The application consists of two main components:

1.  **Server (`server.py`)**:
    * Listens for incoming connections on a specified port.
    * Accepts one client connection at a time.
    * Sends messages to the connected client and receives messages from it.
2.  **Client (`client.py`)**:
    * Connects to the server's hostname and port.
    * Sends messages to the server and receives messages from it.

## Prerequisites

* Python 3.x installed on both the server and client machines.

## Setup and Usage

Follow these steps to get the chat application running:

### 1. Clone the Repository (or download the files)

```bash
git clone https://github.com/Shivamg0520/client-server-chat-application.git
cd client-server-chat-appplication
