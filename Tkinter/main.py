import tkinter

window = tkinter.Tk()
window.title("Not shown")
window.minsize(500, 300)

label = tkinter.Label(text="I am a lable")
label.pack(side="left")

window.mainloop()