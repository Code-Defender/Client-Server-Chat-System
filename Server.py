import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.lower() == 'exit':
        print("Client ended the chat.")
        break
    print("Client:", data)

    msg = input("You: ")
    conn.send(msg.encode())
    if msg.lower() == 'exit':
        print("You ended the chat.")
        break

conn.close()
server_socket.close()
