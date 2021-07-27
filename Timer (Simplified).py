import tkinter as tk
from Timersave import *
from tkinter import ttk


root = tk.Tk()
root.config(bg="black")


t = 0
cln = [Minute, Second]
bn = ["START", "EXIT"]
label = []
b = []
cl = []
option = []


def countdown(count):
    global t
    if t == 0:
        label[0]["text"] = str(cl[1].get()).zfill(2)
        label[1]["text"] = str(cl[0].get()).zfill(2)
    if count >= 0:
        label[0]["text"] = str(count).zfill(2)
        label[1]["text"] = str(t).zfill(2)
        root.after(1000, countdown, count - 1)
    if count < 0:
        if t <= 0:
            t = 0
            b[0].config(state="normal")
        elif t > 0:
            t -= 1
            countdown(59)


for i in range(61):
    option.append(i)
for i in range(2):
    l = tk.Label(root, font=("Helvetica", 169, "bold"), fg="white", bg="black")
    btn = tk.Button(root, text=bn[i], bd=15, bg="black", fg="white")
    CB = ttk.Combobox(root, values=option, width=10)
    CB["state"] = "readonly"
    CB.current(cln[i])
    root.option_add("*TCombobox*Listbox*Background", "black")
    root.option_add("*TCombobox*Listbox*foreground", "white")
    cl.append(CB)
    label.append(l)
    b.append(btn)


def get(Min, Sec):
    global t
    t = int(Min.get())
    Sec = int(Sec.get())
    data = open("Timersave.py", "w")
    data.write(f"Minute = {t}\nSecond = {Sec}")
    data.close()
    countdown(Sec)
    b[0].config(state="disable")


b[0].config(command=lambda: get(cl[0], cl[1]))
b[1].config(command=root.destroy)


label[1].grid()
label[0].grid(row=0, rowspan=14, pady=1000)
cl[0].grid(row=6, sticky="w", padx=100)
cl[1].grid(row=6, sticky="e", padx=100)
b[0].grid(row=6)
b[1].grid(row=6, rowspan=3)
countdown(-1)


root.mainloop()
