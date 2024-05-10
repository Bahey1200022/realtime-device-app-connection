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
        # patient Id  a random value between 1 and 100
        id = random.randint(1, 100)
        for i in range(100):
            time.sleep(0.25)

            # y is a random value between 85 and 99 of "Oxygen level", x is the time interval
            x=i
            y = random.randint(85, 99)
            
            # z is a random value between 60 and 100 of "Heart rate", x is the time interval
            z = random.randint(60, 100)
            
            # t is a random value between 0 and 100 of "Temperature", x is the time interval
            t = random.randint(35, 42)
            
            print(f"Oxygen level: {y}, Heart rate: {z}, Temperature: {t}")

            
            
            
            response = {'x': x, 'y': y, 'z': z,'t':t, 'id': id}
            json_response = json.dumps(response)
            conn.sendall(json_response.encode())
           
                
            # close the connection outside the loop
        conn.close()
        


    
        
        

        




