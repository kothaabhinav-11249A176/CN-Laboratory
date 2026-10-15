import socket

def file_transfer_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    # Get filename from user
    filename = input("Enter the filename to send: ")

    try:
        # Open the file
        with open(filename, 'rb') as file:

            # Send the filename
            client_socket.sendall(filename.encode())

            # Send the file contents
            while True:
                chunk = file.read(1024)

                if not chunk:
                    break

                client_socket.sendall(chunk)

        print(f"File {filename} sent successfully.")

    except FileNotFoundError:
        print(f"File {filename} not found.")

    client_socket.close()


if __name__ == '__main__':
    file_transfer_client()