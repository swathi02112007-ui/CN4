import socket
import subprocess

s = socket.socket()
s.bind(('localhost', 10000))
s.listen(5)

print("Server listening on port 10000...")

c, addr = s.accept()
print(f"Connection from {addr}")

while True:
    try:
        hostname = c.recv(1024).decode('utf-8')

        if not hostname or hostname.lower() == 'exit':
            print("Client disconnected.")
            break

        result = subprocess.run(
            ["ping", hostname],
            capture_output=True,
            text=True
        )

        output = result.stdout

        c.send(output.encode('utf-8'))

    except Exception as e:
        c.send(f"Ping failed: {e}".encode('utf-8'))

c.close()
s.close()