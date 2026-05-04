import tkinter as tk 
from datetime import datetime
def age_calculate():
    try:
        dob_str=entry.get()
        dob=datetime.strptime(dob_str,"%Y-%m-%d")
        today=datetime.today()
        
        age=today.year - dob.year -((today.month,today.day)<(dob.month,dob.day))
        res_label.config(text=f"age :{age} years")
    except:
        res_label.config( "invalid date fromat")
root =tk.Tk()
root.title("Age calulator")
root.geometry("300x200")

label=tk.Label(root, text="enter the date (yyyy-mm-dd)")
label.pack(pady=5)

entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root,text="submit",command=age_calculate)
button.pack(pady=5)

res_label=tk.Label(root,text="")
res_label.pack(pady=5)

root.mainloop()