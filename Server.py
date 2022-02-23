# server.py
import socket 

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 5001 # The port that the client is going to connect to

# bind to the port
serversocket.bind((host, port)) # We can replace the parametere 'host' with the IP Address we want

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("The following Clinet have connected to the server: %s" % str(addr))
    Test = "This is a connection Test!"
    clientsocket.send(Test.encode('ascii'))
    clientsocket.close()
