import customtkinter as s
from tkinter import *
import math

#eventos
def get_input01():
    a = Entry1.get()
    b = Entry2.get()
    c = Entry3.get()
    
    b2 = int(b) * int(b)
    delta = b2 - 4 * int(a) * int(c)
    if delta < 0:
        label5 = s.CTkLabel(window, text="No solution")
        label5.pack()
    else:
        if delta >= 0:
            root = math.sqrt(int(delta))
            bhaskara1 = (- int(b) + int(root)) / 2*int(a)
            bhaskara2 = (- int(b) - int(root)) / 2*int(a)
            result = ("The answer is: ", "x1= ",int(bhaskara1), "and x2= ",int(bhaskara2))
    
    label6 = s.CTkLabel(window, text=" ", font=("arial", 30))
    label6.pack()
    label7 = s.CTkLabel(window, text="x1: ", font=("arial", 30))
    label7.pack()
    label8 = s.CTkLabel(window, text=int(bhaskara1), font=("arial", 30))
    label8.pack()
    label9 = s.CTkLabel(window, text=" ", font=("arial", 30))
    label9.pack()
    label10 = s.CTkLabel(window, text="x2: ", font=("arial", 30))
    label10.pack()
    label11 = s.CTkLabel(window, text=int(bhaskara2), font=("arial", 30))
    label11.pack()


#window
window = s.CTk()
window.title("Equation solver")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)


#texts
label1 = s.CTkLabel(window, text="Second degree equation Solver")
label1.pack()

label2 = s.CTkLabel(window, text="Enter your numbers:")
label2.pack()


#user Input
Entry1 = s.CTkEntry(window, )
Entry1.pack()

Entry2 = s.CTkEntry(window, )
Entry2.pack()

Entry3 = s.CTkEntry(window, )
Entry3.pack()

btn = s.CTkButton(window, text="submit", command=get_input01, width=100, height=30)
btn.pack()


#results
label4 = s.CTkLabel(window, text="Result:")
label4.pack()

window.mainloop()