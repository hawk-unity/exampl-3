from tkinter import *
window = Tk()
window.title("Hawk Application")
lbl = Label(window, text=" Merhaba ", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)
window.geometry("600x290")
txt = Entry(window, width=30)
txt.grid(column=5, row=0)
def clicked():
    res = "Hoşgeldin " + txt.get()
    lbl.configure(text=res)
    clicked()
btn = Button(window, text="Buton'a Bas ", bg="black", fg="white", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
