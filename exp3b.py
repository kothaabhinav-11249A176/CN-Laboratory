kk0import socket


















































































































def echo_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect(('localhost', 65432))

        # Infinite loop to match your continuous terminal input screenshot
        while True:
            # Prompt the user for a message matching your console output layout
            message = input("Enter a message: ")

            # Optional exit check if you want to quit gracefully
            if message.lower() == 'exit':
                break

            # Send message to server
            client_socket.sendall(message.encode())

            # Receive response back from server
            data = client_socket.recv(1024)
            print(f"Echoed from server: {data.decode()}")

    except ConnectionRefusedError:
        print("Could not connect to server. Ensure echo_server is running first.")
    finally:
        client_socket.close()


if __name__ == '__main__':
    echo_client()
