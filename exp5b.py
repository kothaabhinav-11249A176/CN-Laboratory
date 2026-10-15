import socket
import struct
import os
def file_transfer_client():
    filename = input("Enter the filename to send: ").strip()
    if not os.path.isfile(filename):
        print(f"File {filename} not found.")
        return
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 12345))
    except Exception as e:
        print(f"Could not connect to server: {e}")
        return
    try:
        filename_bytes = filename.encode('utf-8')
        header = struct.pack('!I', len(filename_bytes))
        client_socket.sendall(header)
        client_socket.sendall(filename_bytes)
        print(f"Sending {filename}...")
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(65536)
                if not chunk:
                    break
                client_socket.sendall(chunk)
        print(f"File {filename} sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending: {e}")
    finally:
        client_socket.close()
if __name__ == '__main__':
    file_transfer_client()
