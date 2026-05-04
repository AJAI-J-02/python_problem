import tkinter as tk 
from PIL import Image,ImageTk
root=tk.Tk()

img=Image.open("loco.jpeg")
photo=ImageTk.PhotoImage(img)

label=tk.Label(root,image=photo)
label.pack()

root.mainloop()