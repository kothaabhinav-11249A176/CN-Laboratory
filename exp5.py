import socket
import struct
import os


def file_transfer_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")

    try:
        # 1. Read exactly 4 bytes to get the filename length
        header = connection.recv(4)
        if not header:
            return
        filename_len = struct.unpack('!I', header)[0]

        # 2. Read exactly that many bytes to extract the clean filename
        filename = connection.recv(filename_len).decode('utf-8')
        # Extract base name to protect server filesystem from path injection
        safe_filename = os.path.basename(filename)
        print(f"Receiving file: {safe_filename}")

        # 3. Stream the file content in efficient 64KB blocks
        output_path = f"received_{safe_filename}"
        with open(output_path, 'wb') as file:
            while True:
                data = connection.recv(65536)
                if not data:
                    break
                file.write(data)

        print(f"File received and saved as {output_path}")

    except Exception as e:
        print(f"An error occurred during transfer: {e}")
    finally:
        connection.close()
        server_socket.close()


if __name__ == '__main__':
    file_transfer_server()
