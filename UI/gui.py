import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import redis
import json
r = redis.Redis(host='localhost', port=6379, db=0)
x_values = []
y_values = []
def search():
    message_label.config(text="")
    patient_id = patient_id_entry.get()
    data_str = r.get(patient_id)
    if data_str is not None:  # Check if the key exists in Redis

        data = json.loads(data_str)

    # Convert the strings back to arrays
        x_values[:] = json.loads(data['x_values'])
        y_values[:] = json.loads(data['y_values'])
        # print(x_values)
        # print(y_values)
        message_label.config(text=f"patient with ID {patient_id} found")
    else:
        message_label.config(text=f"No data found for patient ID {patient_id}")
            
    
    

def play():
    # Clear the previous plot
    ax.clear()

    # Example: Plot a simple line
    print(x_values)
    ax.plot(x_values, y_values)
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

# Create a placeholder for the plot
figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
plot_placeholder = FigureCanvasTkAgg(figure, root)
plot_placeholder.get_tk_widget().pack()

root.mainloop()