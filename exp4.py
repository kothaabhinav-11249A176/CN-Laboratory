import socket
import threading

# Initialize global client list and a thread lock to prevent race conditions
clients = []
clients_lock = threading.Lock()


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    try:
        while True:
            # Receive message payload
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Received from {client_address}: {message}")

            # Safely broadcast to all other active clients using the lock
            with clients_lock:
                for client in clients:
                    if client != client_socket:
                        try:
                            client.sendall(message.encode('utf-8'))
                        except Exception as send_error:
                            print(f"Failed sending to a client: {send_error}")

    except Exception as e:
        print(f"Error with {client_address}: {e}")

    finally:
        # Guarantee removal and cleanup regardless of how the loop exited
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)

        client_socket.close()
        print(f"{client_address} disconnected")


def chat_server():
    # Setup TCP Server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to localhost on port 55555
    server_socket.bind(('127.0.0.1', 55555))
    server_socket.listen(5)
    print("Server listening on port 55555...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()

            # Safely append the new client using the lock
            with clients_lock:
                clients.append(client_socket)

            # Spawn daemon thread so it exits automatically when the server stops
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.daemon = True
            thread.start()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            break


if __name__ == '__main__':
    chat_server()
