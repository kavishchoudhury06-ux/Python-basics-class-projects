from tkinter import *

root = Tk()

root.title("Sample frame")
root.geometry("400x400")

def display():
    
    namedisplay = nameEntry.get()
    greeting = "Hello "+namedisplay
    message = "\nYou have created an account"
    textDisplay.insert(END, greeting)
    textDisplay.insert(END, message)
    

frame = Frame(master=root, bg="lightblue", height=200, width=360 )
frame.place(x=20, y=0)

name = Label(master=frame, text="Name", bg = "blue", fg = "white", width=12)
email = Label(master=frame, text="Email ID", bg = "blue", fg = "white", width=12)
password = Label(master=frame, text="Password", bg = "blue", fg = "white", width=12)


name.place(x=20, y=20)
email.place(x=20, y=80)
password.place(x=20, y=140)

nameEntry = Entry(master=frame, bg="lightgrey", fg="black")
emailEntry = Entry(master=frame, bg="lightgrey", fg="black")
passwordEntry = Entry(master=frame, bg="lightgrey", fg="black", show="#")
nameEntry.place(x=150, y=20)
emailEntry.place(x=150, y=80)
passwordEntry.place(x=150, y=140)
button = Button(text="Create account", bg="blue", fg="white", command=display)
button.place(x=130, y=210)

textDisplay = Text(bg="lightgrey", fg="black")
textDisplay.place(y=250)
root.mainloop()
