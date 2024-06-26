import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import redis
import json
import matplotlib.animation as animation

r = redis.Redis(host='localhost', port=6379, db=0)
x_values = []
y_values = []
z_values = []
t_values = []

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,
def search():
    message_label.config(text="")
    patient_id = patient_id_entry.get()
    data_str = r.get(patient_id)
    if data_str is not None:  # Check if the key exists in Redis

        data = json.loads(data_str)

    # Convert the strings back to arrays
        x_values[:] = json.loads(data['x_values'])
        y_values[:] = json.loads(data['y_values'])
        z_values[:] = json.loads(data['z_values'])
        t_values[:] = json.loads(data['t_values'])
        # print(x_values)
        # print(y_values)
        message_label.config(text=f"patient with ID {patient_id} found")
    else:
        message_label.config(text=f"No data found for patient ID {patient_id}")
            
    
    

def play():
    
    # Clear the previous plot
    # Clear the previous plot
    ax.clear()

    # Create a line object with no data
    line, = ax.plot([], [], 'r-')

    ani = animation.FuncAnimation(figure, update, len(x_values), fargs=[x_values, y_values, line],
                                  interval=100, blit=True)
    ax.set_xlim(0, max(x_values))
    ax.set_ylim(min(y_values), max(y_values))
    ax.set_xlabel('Time')
    ax.set_ylabel('Oxygen Level')

    plot_placeholder.draw()
    
def play2():
    # Clear the previous plot
    ax.clear()

    # Create a line object with no data
    line, = ax.plot([], [], 'r-')

    ani = animation.FuncAnimation(figure, update, len(x_values), fargs=[x_values, z_values, line],
                                  interval=100, blit=True)
    ax.set_xlim(0, max(x_values))
    ax.set_ylim(min(z_values), max(z_values))
    ax.set_xlabel('Time')
    ax.set_ylabel('Heart Rate')

    plot_placeholder.draw()
def play3():
    # Clear the previous plot
    ax.clear()

    # Create a line object with no data
    line, = ax.plot([], [], 'r-')

    ani = animation.FuncAnimation(figure, update, len(x_values), fargs=[x_values, t_values, line],
                                  interval=100, blit=True)
    ax.set_xlim(0, max(x_values))
    ax.set_ylim(min(t_values), max(t_values))
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')

    plot_placeholder.draw()
    
root = tk.Tk()
root.title("Patient Vital Signs Viewer")

# Create a search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

message_label = tk.Label(root, text="")
message_label.pack()

patient_id_entry = tk.Entry(search_frame)
patient_id_entry.pack(side=tk.LEFT)



# Create a search button
search_button = tk.Button(search_frame, text="Patient ID", command=search)
search_button.pack(side=tk.LEFT)

# Create a play button
play_button = tk.Button(root, text="Show Oxygen Levels", command=play)
play_button.pack()

# Create a button to plot heart rate
play2_button = tk.Button(root, text="Show Heart Rate", command=play2)
play2_button.pack()

# Create a button to plot temperature
play3_button = tk.Button(root, text="Show Temperature", command=play3)
play3_button.pack()

# Create a placeholder for the plot
figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
plot_placeholder = FigureCanvasTkAgg(figure, root)
plot_placeholder.get_tk_widget().pack()

root.mainloop()