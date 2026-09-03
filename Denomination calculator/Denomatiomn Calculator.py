from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



# Setup Root Window
window = Tk()
window.title("Codingal's toplevel")
window.configure(bg="light blue")
window.geometry("600x600")

upload = Image.open("image.png")
upload = upload.resize((240, 300))
image = ImageTk.PhotoImage(upload)

label1 = Label(window, text="Hey user, Welcome To The Denomination Calculator Application", bg="lightblue")
label1.place(anchor="center", relx=0.5, y=340)

label = Label(window, image=image, bg="light blue")
label.place(x=180, y=20)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label = Label(top, text="Enter total amount", bg="light grey")

    label.place(x=210, y=50)
    entry = Entry(top)
    entry.place(x=200, y=80)
    
    def calculator():
        try:
            amount = int(entry.get())
            note1000 = amount // 1000
            note500 = amount // 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    btn = Button(top, text="Calculate", bg="brown", fg="white", command=calculator)
    btn.place(x=240, y=120)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light grey")
    lbl.place(x=140, y=170)


    l1 = Label(top, text="1000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)


    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
    
    

button1 = Button(master=window , text="Lets get Started", bg="brown", fg="white", command=topwin )
button1.place(x=260, y=360)
window.mainloop()