import socket
import threading
import sys
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\nDisconnected from server.")
                break
            print(f"\n{message}")
        except:
            break
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 55555))
    except Exception as e:
        print(f"Could not connect to server: {e}")
        return
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.daemon = True
    recv_thread.start()
    print("Connected! Type your messages below (or type 'exit' to quit):")
    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        if msg.strip():
            try:
                client.sendall(msg.encode('utf-8'))
            except:
                break
    client.close()
if __name__ == '__main__':
    start_client()