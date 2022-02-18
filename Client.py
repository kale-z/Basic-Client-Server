# client.py
import socket

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 5001 # The port that the server is connected to

# connection to hostname on the port.
server.connect((host, port)) # Here also we can add the IP Address that we want to connect to instead of 'host'

# Receive no more than 1024 bytes
message = server.recv(1024)
server.close()
print(message.decode('ascii'))
