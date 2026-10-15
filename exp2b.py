import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

# Create a basic HTTP GET request
http_request = (
    "GET / HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# Send the request to the HTTP server
client.sendall(http_request.encode())

# Gather all data sent back by the server
response = b""
while True:
    # Read data in chunks of 4096 bytes
    chunk = client.recv(4096)
    if not chunk:
        break
    response += chunk

# Close the socket connection
client.close()

# Print the formatted output exactly as shown in the console image
print("--- Received HTTP Response ---")
print(response.decode('utf-8'))
