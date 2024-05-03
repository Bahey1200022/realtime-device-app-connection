import socket

SERVER_ADDRESS='192.168.1.12'
PORT=2001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS,PORT))

# to run :python frontend.py  cd server_app
    
    data='lab-dist'
    front_socket.sendall(data.encode()) 
    response=front_socket.recv(1024)
    print('trial'+response.decode())
    
