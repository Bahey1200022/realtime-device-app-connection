import socket
import random
import json
import time
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
        id = random.randint(1, 100)
        for i in range(100):
            time.sleep(0.25)

            x=i
            y = random.randint(85, 99)
            
            
            response = {'x': x, 'y': y, 'id': id}
            json_response = json.dumps(response)
            conn.sendall(json_response.encode())
           
                
            # close the connection outside the loop
        conn.close()
        


    
        
        

        




