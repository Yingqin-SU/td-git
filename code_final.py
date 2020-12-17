import tkinter as tk

nombre1 = ''

def ajout(nombre_ajouté):
    global nombre1
    nombre1 += nombre_ajouté
    label['text'] = nombre1

def nombre_1():
    ajout('1')

def nombre_2():
    ajout('2')

def nombre_3():
    ajout('3')

def nombre_4():
    ajout('4')

def nombre_5():
    ajout('5')

def nombre_6():
    ajout('6')

def nombre_7():
    ajout('7')

def nombre_8():
    ajout('8')

def nombre_9():
    ajout('9')

def nombre_0():
    ajout('0')

def addition():
    global nombre1, nombre2, op
    nombre2 = float(nombre1)
    nombre1 = ''
    op = 1

def soustraction():
    global nombre1, nombre2, op
    nombre2 = float(nombre1)
    nombre1 = ''
    op = 2

def multiplication():
    global nombre1, nombre2, op
    nombre2 = float(nombre1)
    nombre1 = ''
    op = 3

def division():
    global nombre1, nombre2, op
    nombre2 = float(nombre1)
    nombre1 = ''
    op = 4

def egale():
    global nombre1, nombre_final
    nombre1 = float(nombre1)
    if op == 1:
        nombre_final = nombre2 + nombre1
    elif op == 2:
        nombre_final = nombre2 - nombre1
    elif op == 3:
        nombre_final = nombre2 * nombre1
    elif op == 4:
        nombre_final = nombre2 / nombre1
    nombre1 = nombre_final
    label['text'] = nombre1

def effacer():
    global nombre1
    nombre1 = ''
    label['text'] = nombre1

main = tk.Tk()
main.geometry("400x300+400+300")
main.title('calc')

label = tk.Label(main, text='0')
label.grid(column=0, row=0, rowspan = 2, columnspan = 2)

button_1 = tk.Button(main, text="1", command=nombre_1)
button_1.grid(column=1, row=6)
button_2 = tk.Button(main, text="2", command=nombre_2)
button_2.grid(column=2, row=6)
button_3 = tk.Button(main, text="3", command=nombre_3)
button_3.grid(column=3, row=6)
button_4 = tk.Button(main, text="4", command=nombre_4)
button_4.grid(column=1, row=5)
button_5 = tk.Button(main, text="5", command=nombre_5)
button_5.grid(column=2, row=5)
button_6 = tk.Button(main, text="6", command=nombre_6)
button_6.grid(column=3, row=5)
button_7 = tk.Button(main, text="7", command=nombre_7)
button_7.grid(column=1, row=4)
button_8 = tk.Button(main, text="8", command=nombre_8)
button_8.grid(column=2, row=4)
button_9 = tk.Button(main, text="9", command=nombre_9)
button_9.grid(column=3, row=4)
button_0 = tk.Button(main, text="0", command=nombre_0)
button_0.grid(column=2, row=7)

button_multiplier = tk.Button(main, text="*", command=multiplication)
button_multiplier.grid(column=4, row=5)

button_diviser = tk.Button(main, text="/", command=division)
button_diviser.grid(column=4, row=4)

button_ajouter = tk.Button(main, text="+", command=addition)
button_ajouter.grid(column=4, row=6)

button_soustraire = tk.Button(main, text="-", command=soustraction)
button_soustraire.grid(column=4, row=7)

button_effacer = tk.Button(main, text="C", command=effacer)
button_effacer.grid(column=1, row=7)

button_egal = tk.Button(main, text="=", command=egale)
button_egal.grid(column=3, row=7)


main.mainloop()