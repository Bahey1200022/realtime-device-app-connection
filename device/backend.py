import socket

HOST= '0.0.0.0'

PORT=2001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as app_socket:
    app_socket.bind((HOST,PORT))
    app_socket.listen()

    print((HOST,PORT))

#to run :python backend.py  cd device
    conn,add=app_socket.accept()
    with conn:
        print('ip',add)  

        data=conn.recv(1024) 

        print('data:',data.decode())
        response='socket-connection'+data.decode()
        conn.sendall(response.encode())
        


    
        
        

        




