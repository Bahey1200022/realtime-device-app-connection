import socket
import json

SERVER_ADDRESS='192.168.1.12'
PORT=2001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS,PORT))

    # receive the data from the server
    while True:
        data = front_socket.recv(1024)
        if not data:
            break
           
        response = data.decode()
        print(response)
    
    # close the connection
    front_socket.close()
    
    
    
    
