try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
import random
import os

root = Tk()
root.geometry("600x600+230+180")
root.title('Piedra Papel Tijeras Lagarto Spock')
frame1 = Frame(root)
frame1.grid(row = 0, column = 0)
canvas = Canvas(root,width=500, height=520)
canvas.grid(row = 0, column = 1)
rb_var = IntVar()
rb_mode_var = IntVar()
rb_var.set(" ")
player_ganadas = 0
comp_ganadas = 0
ties = 0

FILL_CIRCLES = "#FFF8DC"
C_GUESS = '#FF69B4'
PLAYER_GUESS = '#87CEFA'
TIE_COLOR = '#FFD700'
CIRCLE_FONT = "Verdana 10"
F_HEL_12 = "Arial 12"
LAB_WIDTH = 14
FUDGE = 3

#Defino variables de imagenes
imagen1=PhotoImage(file="photo1.pgm")   #Piedra
imagen2=PhotoImage(file="photo2.pgm")   #Tijera
imagen3=PhotoImage(file="photo3.pgm")   #Lagarto
imagen4=PhotoImage(file="photo4.pgm")   #Spock
imagen5=PhotoImage(file="photo5.pgm")   #Papel

#Definimos las variables en 0
def reset_scores():
    global player_ganadas, comp_ganadas, empate
    #Resetea valores
    player_ganadas = 0
    comp_ganadas = 0
    empate = 0
    update_scores()

#sumar los puntajes
def update_scores():
    global player_wins, comp_wins, empate
    global player_ganadas, comp_ganadas, ties
    #Cuenta partidas ganadas, perdidas o empates
    t_disp.delete(0.0, END)
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Tu = \t" + str(player_ganadas))
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Sheldon = \t" + str(comp_ganadas))
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Empates  = \t" + str(ties))
    t_disp.insert(END, '\n')

def play_game():
    global player_ganadas, comp_ganadas, ties
    global t_rules1,t_rules2
    player_pick = rb_var.get()
    comp_number = random.randrange(0,5)
    
    if  (player_ganadas + comp_ganadas + ties) % FUDGE == 0:
        if player_pick == 4:
            comp_number = 1
        else:
            comp_number = player_pick + 1
            messagebox.showinfo("Perdiste", message="No pudiste contra mi astucia JAJAJAJAJAJAJAJAJAJAJJAJAJAJJAJAJAJAJJA")
            
    diff = (comp_number - player_pick) % 5
    if diff == 0:
        ties = ties + 1
        messagebox.showinfo("Emapte", message="RAYOOOOOOS!!!")

    elif diff == 3 or diff == 4:
            player_ganadas = player_ganadas + 1
            messagebox.showinfo("Ganaste", message="Admito mi derrota :(")
    else:
        comp_ganadas = comp_ganadas + 1
        messagebox.showinfo("Perdiste", message="No pudiste contra mi astucia")
        os.system('\a')

    update_scores()

def play_access():

    global player_wins, comp_wins, empate
    global player_ganadas, comp_ganadas, ties
    global t_rules1,t_rules2

    #Leo datos ingresados
    us = in1.get()
    ps = in2.get()
     
    if us=="user" and ps=="1234": #Si cumplen estos datos

        #Invoco imagenes
        lglimagen1=Label(root,height=100,width=100,image=imagen1).place(x=365,y=100)
        lglimagen2=Label(root,height=100,width=100,image=imagen2).place(x=240,y=180)
        lglimagen3=Label(root,height=100,width=100,image=imagen3).place(x=300,y=300)
        lglimagen4=Label(root,height=100,width=100,image=imagen4).place(x=490,y=180)
        lglimagen5=Label(root,height=100,width=100,image=imagen5).place(x=440,y=300)

    else:
        
        messagebox.showinfo("Error",message="Ingrese un usuario correcto")


def Ver_Reglas(): #Genera ventana de reglas
    ventana2 = Toplevel()
    ventana2.wm_geometry("280x250")
    prom = Label(ventana2,text="Reglas: \n\nPiedra aplasta a lagarto o tijera\nTijera corta al papel y decapita al lagarto\nSpock rompe a la tijera o explota piedra\nLagarto envenena Spock o come Papel\nPapel envuelve piedra o ahoga Spock "
    ,font=("Arial",10)).place(x=5,y=5)

def Ver_Historia():#Genera ventana de historia
    ventana3 = Toplevel()
    ventana3.wm_geometry("350x300")
    prom = Label(ventana3,text="Historia: \n\nSheldon ha modificado el piedra \npapel o tijera convencional, ahora tendras que \nvencerlo en supropio juego. SUERTEEEEE ",font=("Arial",10)).place(x=50,y=5)

#Creacion de ingreso de datos para usuarios
L_sel0 = Label(frame1, text="Ingresar usuario antes de jugar:")
L_sel0.grid(column = 0, row = 0, pady = 2, sticky=W)
L_sel1 = Label(frame1, text="Usuario:")
L_sel1.grid(column = 0, row = 1, pady = 2, sticky=W)
in1 = StringVar()
camp1 = Entry(frame1,textvariable=in1).place(x=50,y=25)
L_sel2 = Label(frame1, text="Pass:")
L_sel2.grid(column = 0, row = 2, pady = 2, sticky=W)
in2 = StringVar()
camp2 = Entry(frame1,textvariable=in2,show="*").place(x=50,y=50)
b_play = Button(frame1, text='Ingresar', command=play_access, width = LAB_WIDTH, background = "white")
b_play.grid(row = 3, column = 0)

#Radio button
L_sel3 = Label(frame1, text="Elige una", width = 12)
L_sel3.grid(row = 4, column = 0, pady = 2)
rb_Piedra = Radiobutton(frame1, text="Piedra",variable = rb_var, value=0, width = LAB_WIDTH, pady = 2,anchor = W)
rb_Piedra.grid(row = 5, column = 0)
rb_Papel = Radiobutton(frame1, text ="Papel",variable = rb_var, value=2, width = LAB_WIDTH, pady = 2, anchor = W)
rb_Papel.grid(row = 6, column = 0)
rb_Tijera = Radiobutton(frame1, text = "Tijera",variable = rb_var, value=4, width = LAB_WIDTH,pady = 2, anchor = W)
rb_Tijera.grid(row = 7, column = 0)
rb_lagarto = Radiobutton(frame1, text = "Lagarto",variable = rb_var, value=3, width = LAB_WIDTH,pady = 2, anchor = W)
rb_lagarto.grid(row = 8, column = 0)
rb_Spock = Radiobutton(frame1, text = "Spock",variable = rb_var, value=1, width = LAB_WIDTH, pady = 2,anchor = W)
rb_Spock.grid(row = 9, column = 0)

#Score
b_play = Button(frame1, text='Presione para jugar', command=play_game, width = LAB_WIDTH, background = "white")
b_play.grid(row = 10, column = 0)
Lblank2 = Label(frame1, text="", width = LAB_WIDTH)
Lblank2.grid(column = 0, row = 11)
L_score = Label(frame1, text="Scores", width = LAB_WIDTH)
L_score.grid(column = 0, row = 12)
t_disp = Text(frame1, width = LAB_WIDTH, height = 5)
t_disp.grid(row = 13, column = 0)

#Espacios en blanco
Lblank_text = Label(frame1, text="", width = LAB_WIDTH)
Lblank_text.grid(column = 0, row = 14)
Lblank_mode = Label(frame1, text="", width = 12)
Lblank_mode.grid(column = 0, row = 16)
Lblank_mode2 = Label(frame1, text="", width = 12)
Lblank_mode2.grid(column = 0, row = 18)

#Botones de Reglas e Historia
b_rules = Button(frame1, text='Reglas',command=Ver_Reglas, width = LAB_WIDTH, background = "white")
b_rules.grid(row = 15, column = 0)
b_story = Button(frame1, text='Historia', command=Ver_Historia, width = LAB_WIDTH, background = "white")
b_story.grid(row = 17, column = 0)

L_sel_mode = Label(frame1, text="Selecciona modo", width = 12)
L_sel_mode.grid(row = 20, column = 0)

def quit_this():
    root.quit()
    root.destroy()

#Boton de salida
rb_Quit = Radiobutton(frame1, text = "QUIT", variable = rb_mode_var, value=3,
    command = quit_this, width = LAB_WIDTH, indicatoron=0)
rb_Quit[ "fg" ] = "DarkRed"
rb_Quit[ "bg" ] = "Bisque"
rb_Quit.grid(row = 21, column = 0)

mainloop()
