from tkinter import *
from tkinter import messagebox

# Step 2: Create main window
root = Tk()

# Step 3: Set window size
root.title("Scan for Viruses")
root.geometry("200x200")

# Step 4: Function to show warning message
def msg():
    messagebox.showwarning("Warning", "Stop! Virus Found.", icon="error")

# Step 5: Create button
button = Button(root, text="Scan for Virus", command=msg)

# Step 6: Place button on window
button.place(x=40, y=80)

# Step 7: Start event loop
root.mainloop()
