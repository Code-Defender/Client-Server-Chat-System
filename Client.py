import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print("Connected to the server.")

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    if msg.lower() == 'exit':
        print("You ended the chat.")
        break

    data = client_socket.recv(1024).decode()
    if data.lower() == 'exit':
        print("Server ended the chat.")
        break
    print("Server:", data)

client_socket.close()
