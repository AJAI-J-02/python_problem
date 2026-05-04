import tkinter as tk
def say_hello():
    label.config(text="you cliked meeeeeeee")

root=tk.Tk()
root.title("gutton click")

label=tk.Label(root,text="click o it")
label.pack()

button=tk.Button(root,text="clike meee",command=say_hello)
button.pack()

root.mainloop()