import socket
import json
import matplotlib.pyplot as plt
import redis
SERVER_ADDRESS = '192.168.1.11'
PORT = 2001
x_values = []
y_values = []
#plt.ion()  # Turn on interactive mode

# Connect to your Redis server
r = redis.Redis(host='localhost', port=6379, db=0)
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
x_values_str = json.dumps(x_values)
y_values_str = json.dumps(y_values)

# Store the arrays in Redis
r.set(id, json.dumps({'x_values': x_values_str, 'y_values': y_values_str}))