import socket


def echo_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to localhost on port 65432
    server_socket.bind(('localhost', 65432))
    # Listen for connections
    server_socket.listen(1)
    print("Server listening on port 65432...")

    try:
        # Accept a connection from the client
        connection, client_address = server_socket.accept()
        print(f"Connected by {client_address}")

        while True:
            # Receive data from the client
            data = connection.recv(1024)
            if not data:
                break  # Exit loop if client closes connection

            print(f"Received: {data.decode().strip()}")
            # Echo the data directly back to the client
            connection.sendall(data)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
        server_socket.close()


if __name__ == '__main__':
    echo_server()

