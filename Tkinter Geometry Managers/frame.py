from tkinter import *

root = Tk()

root.title("Sample frame")
root.geometry("500x500")

frame = Frame(master=root, bg="grey", height=100, width=50, relief=RAISED, borderwidth=10)
frame.pack()
root.mainloop()