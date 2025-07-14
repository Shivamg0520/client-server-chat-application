import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()

while True:
    messages_to_client = str(input("Server: "))
    client.send(bytes(messages_to_client,"utf-8"))
    messages_from_client = client.recv(100)
    print("client: " + messages_from_client.decode("utf-8"))