try:
    from tkinter import *
except ImportError:
    from Tkinter import *
root = Tk()
root.geometry("600x520+230+180")
piedra1=PhotoImage(file="piedra1.pgm")
etiqueta=Label(root,image=piedra1).place(x=100,y=100)
mainloop()

etiqueta = Label(root, image=piedra1,width=100,height=100,anchor=CENTER).place(x=20, y=20)
etiqueta = Label(root, image=piedra1,width=100,height=100,anchor=CENTER)
