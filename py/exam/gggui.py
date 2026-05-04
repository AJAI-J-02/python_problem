import tkinter as tk

root=tk.Tk()
root.title("welcome ")
root.geometry("300x100")

label = tk.Label(text="Hello World!")

label.pack(pady=20)


root.mainloop()