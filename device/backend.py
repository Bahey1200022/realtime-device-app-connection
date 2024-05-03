import socket
from signal import generate_ecg_signal
import random
import json
#### here we are emulating the medical device
HOST= '0.0.0.0'

PORT=2001

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as app_socket:
    app_socket.bind((HOST,PORT))
    app_socket.listen()

    print((HOST,PORT))

#to run : python backend.py  cd device
    conn,add=app_socket.accept()
    with conn:
        print('ip',add)  
        x, y = generate_ecg_signal()
        id = random.randint(1, 100)
        
        response = {'x': x.tolist(), 'y': y.tolist(), 'id': id}
        json_response = json.dumps(response)
        conn.sendall(json_response.encode())
        


    
        
        

        




