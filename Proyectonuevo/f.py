try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
root = Tk()
root.geometry("600x520+230+180")
root.title('Piedra Papel Tijeras Lagarto Spock')
def contar_hist():
    messagebox.showinfo("Este es el reto de Sheldon Cooper"
                        ,message="Esta es una variacion del famoso juego Piedra, papel y tijera, creador por el famoso personaje Sheldon Cooper, tu objetivo es ganarle en su propio juego: Piedra, papel, tijera, Lagarto y Spock .")

btn_his=Button(root,command=contar_hist(),text="Historia",height=2,width=20).place(x=400, y=20)
mainloop()