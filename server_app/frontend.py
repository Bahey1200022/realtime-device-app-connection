import socket
import json
import matplotlib.pyplot as plt

SERVER_ADDRESS = '192.168.1.12'
PORT = 2001

plt.ion()  # Turn on interactive mode

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as front_socket:
    front_socket.connect((SERVER_ADDRESS, PORT))

    # Create empty lists to store x and y values
    x_values = []
    y_values = []

    # Receive the data from the server
    while True:
        data = front_socket.recv(1024)
        if not data:
            break

        response = data.decode()
        data = json.loads(response)
        id = data['id']
        x = data['x']
        y = data['y']

        # Append x and y values to the lists
        x_values.append(x)
        y_values.append(y)

        # Clear the plot and plot the new data
        plt.clf()
        plt.plot(x_values, y_values)
        plt.draw()
        plt.pause(0.01)  # Pause to allow the plot to update

    # Close the connection
    front_socket.close()

plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final plot