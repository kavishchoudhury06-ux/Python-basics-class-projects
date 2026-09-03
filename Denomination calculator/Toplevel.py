from tkinter import *

# Setup Root Window
window = Tk()
window.title("Codingal's toplevel")
window.geometry("600x600")

def top():
    Top = Toplevel()
    Top.title("toplevel window")
    Top.geometry("200x200")
    Top.mainloop
    
button = Button(master=window , text="Click me!", command=top)
button.pack()
window.mainloop()