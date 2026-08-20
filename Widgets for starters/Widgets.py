from tkinter import *
from datetime import date 
screen = Tk()
screen.title("My first window")
screen.geometry("500x500")

def display():
    name = name_input.get()
    greeting = "Hello " + name + "\n"
    db.insert(END, greeting)
    message = "Welcome to the application \n"
    db.insert(END, message)
    todayDate = date.today()
    db.insert(END, todayDate)
    

heading = Label(text="Welcome", fg="blue", bg="green", width=50, height=3,font =5)
heading.pack()

inst = Label(text="Enter your name below", fg="black", bg="pink", width=50, height=3,font =5)
inst.pack()

name_input = Entry(width = 25,font =5)
name_input.pack()

btn = Button(text="start", fg="green", bg="blue" ,font =5, command=display)
btn.pack()

db = Text(height=6)
db.pack()
screen.mainloop()