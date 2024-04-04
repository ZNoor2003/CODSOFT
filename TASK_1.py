
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("TO-DO-LIST-APP")
root.geometry("800x650+300+10")
root.config(bg ="#F4ECF7")

label_1 = Label(root, text="===>TO-DO-LIST-APPLICATION<===", font=("Times New Roman", 25, "bold"), width=10, bd=5, bg="#9C6DA5", fg="white")
label_1.pack(side="top", fill=BOTH)

label_2 = Label(root, text="ADD TASK", font=("Times New Roman", 16, "bold"), width=10, bd=5, bg="#9C6DA5", fg="white")
label_2.place(x=340, y=60)

label_3 = Label(root, text="TO-DO LIST", font=("Times New Roman", 16, "bold"), width=10, bd=5, bg="#9C6DA5", fg="white")
label_3.place(x=340, y=250)

listbox = Listbox(root, height=14, bd=5, width=32, font=("Times New Roman", 14, "bold "))
listbox.place(x=240, y=290)

text = Text(root, bd=5, height=1, width=30, font=("Times New Roman", 14, "bold"))
text.place(x=250, y=100)

def add():
    content = text.get(1.0, END).strip()
    if content:
        listbox.insert(END, content)
        with open('list.txt', 'a') as file:
            file.write(content + '\n')
        text.delete(1.0, END)

def delete():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in selected_indices[::-1]:
            listbox.delete(index)
        with open('list.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() not in listbox.get(0, END):
                    file.write(line)
            file.truncate()

def update():
    selected_index = listbox.curselection()
    if selected_index:
        content = text.get(1.0, END).strip()
        listbox.delete(selected_index)
        listbox.insert(selected_index, content)
        text.delete(1.0, END)
        with open('list.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != listbox.get(selected_index):
                    file.write(line)
                else:
                    file.write(content + '\n')
            file.truncate()

button_1 = Button(root, text="ADD", font=("Times New Roman", 16, "bold italic"), width=10, bd=5, bg="#2980B9", fg="white", command=add)
button_1.place(x=200, y=150)

button_2 = Button(root, text="UPDATE", font=("Times New Roman", 16, "bold italic"), width=10, bd=5, bg="#27AE60", fg="white", command=update)
button_2.place(x=340, y=150)

button_3 = Button(root, text="DELETE", font=("Times New Roman", 16, "bold italic"), width=10, bd=5, bg="#C0392B", fg="white", command=delete)
button_3.place(x=480, y=150)

try:
    with open('list.txt', 'r') as file:
        for line in file:
            listbox.insert(END, line.strip())
except FileNotFoundError:
    pass

root.mainloop()
