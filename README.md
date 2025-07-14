
# Python Socket Chat Application

This is a simple client-server chat application built using Python’s `socket` library. It demonstrates basic socket programming concepts by allowing two-way communication between a server and a client over TCP.

## 📂 Project Structure

- `server.py`: Runs the server that waits for client connections and enables message exchange.
- `client.py`: Connects to the server and allows the user to chat interactively.

## 🚀 Features

- Simple TCP socket communication.
- Real-time bidirectional messaging between server and client.
- Runs on localhost using the host’s network name and port `12345`.

## 🛠️ Requirements

- Python 3.x

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Run the server**
   Open a terminal and start the server:
   ```bash
   python server.py
   ```

3. **Run the client**
   Open another terminal (or run on a different machine in the same network) and start the client:
   ```bash
   python client.py
   ```

4. **Start chatting!**
   - Server and client can send messages to each other interactively.

## 📌 Notes

- Both scripts use `socket.gethostname()` which works on localhost. For remote connections, replace `HOST_NAME` with the server’s IP address.
- Only **one client** can connect at a time in this simple version.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
