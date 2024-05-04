import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def search():
    patient_id = patient_id_entry.get()
    # Add your search functionality here using the patient_id
    pass

def play():
    # Clear the previous plot
    ax.clear()

    # Example: Plot a simple line
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    ax.plot(x, y)
    plot_placeholder.draw()

root = tk.Tk()

# Create a search bar
search_frame = tk.Frame(root)
search_frame.pack()

patient_id_entry = tk.Entry(search_frame)
patient_id_entry.pack(side=tk.LEFT)

# Create a search button
search_button = tk.Button(search_frame, text="Search ID", command=search)
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