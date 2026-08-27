from tkinter import *

# Step 2: Create main window
window = Tk()


window.title("Event Handler")
window.geometry("200x200")


    
def keypress(event):
    print(event.char)
    
def buttonclick():
    print("The button is clicked")
    


    
    
button = Button(text="Click me", font=3, command=buttonclick)
button.place(x=40, y=80)

window.bind("<Key>", keypress)
    

window.mainloop()
