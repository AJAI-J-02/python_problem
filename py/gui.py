import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Hello world")
root.geometry("300x100")  # width x height

# Add a label
label = tk.Label(text="Hello gui")
label.pack(pady=10)  # center with some padding

# Run the GUI
root.mainloop()