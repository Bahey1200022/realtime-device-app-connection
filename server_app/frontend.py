import socket
import json

SERVER_ADDRESS='192.168.1.12'
PORT=2001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS,PORT))

# to run : python frontend.py  cd server_app
    
    # receive the data from the server
    response = b""
    while True:
        data = front_socket.recv(1024)
        if not data:
            break
        response += data
    response = response.decode()
    id = json.loads(response)['id']
    x = json.loads(response)['x']
    y = json.loads(response)['y']
    print('x:',x)
    print('y:',y)
    print('id:',id)
    
    
    
    
