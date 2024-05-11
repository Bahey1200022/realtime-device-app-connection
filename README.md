<h1>Real-Time Medical Data Monitoring System</h1>
<p>This project simulates a real-time medical data monitoring system that includes a medical device simulator, a server application, and a GUI for data visualization. The medical device simulator continuously generates random vital sign data (Oxygen Level) and sends it to the server. The server stores the data in a Redis database, and the GUI allows users to search for specific patient data and visualize it.</p>
<h2>Technologies</h2>
<p>
    Programming Language: Python
    Database: Redis
    GUI Framework: Tkinter
    Networking: Socket programming (TCP)
</p>
<h2>Project Description</h2>

<p>
Medical Device Simulator (Client):
        Simulates a medical device generating random vital sign data (Oxygen Level & temperature & Heart Beat).
        Sends patient ID and vital sign data to the server at regular intervals using a TCP socket connection.

Server:
        Listens for incoming connections from client devices using a TCP socket.
        Connects to a Redis database to store received data as key-value pairs (key: patient ID, value: vital signs).

GUI (Data Visualization):
        Provides a user-friendly interface to visualize Oxygen level & temperature & Heart Beat over time.
        Allows users to search for specific patients using their ID.





https://github.com/Bahey1200022/realtime-device-app-connection/assets/104398513/31f2773d-891a-46b1-8d27-60abe1af18e7




        Displays corresponding vital sign data from Redis in a plot.

</p>
