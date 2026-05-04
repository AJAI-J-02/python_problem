import tkinter as tk

def show_text():
    user_input=entry.get()
    label.config(text="user input "+user_input)

root=tk.Tk()
root.title(" guiii")
root.geometry("500x500")

entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="submit",command=show_text)
button.pack()

label=tk.Label(root,text="")
label.pack()

root.mainloop()