import socket
import json
import matplotlib.pyplot as plt

SERVER_ADDRESS = '192.168.1.12'
PORT = 2001
x_values = []
y_values = []
#plt.ion()  # Turn on interactive mode

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS, PORT))

    # Create empty lists to store x and y values
    

    # Receive the data from the server
    while True:
        data = front_socket.recv(1024)
        if not data:
            break

        response = data.decode()
        data = json.loads(response)
        print(data)
        id = data['id']
        x = data['x']
        y = data['y']
        
        
        x_values.append(x)
        y_values.append(y)

        

    # Close the connection
    front_socket.close()


#TODO: SAVE TO REDIS DB
