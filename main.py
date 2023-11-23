from tkinter import *
from tkinter import END
from tkinter import font
from tkinter import messagebox
import fileWrite

fNum = 0
sNum = 0
result = 0
math = ""

# Függvenyek


def btnClear():
    e.delete(0, END)


def btnCl(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def btnAdd():
    global fNum
    global math
    fNum = e.get()
    math = "+"
    e.delete(0, END)


def btnSub():
    global fNum
    global math
    math = "-"
    fNum = e.get()
    e.delete(0, END)


def btnMulti():
    global fNum
    global math
    fNum = e.get()
    math = "*"
    e.delete(0, END)


def btnDiv():
    global fNum
    global math
    fNum = e.get()
    math = "/"
    e.delete(0, END)


def btnCalculate():
    sNumber = e.get()
    global sNum
    global result
    sNum = int(sNumber)
    e.delete(0, END)
    if math == "+":
        result = int(fNum) + int(sNum)
    elif math == "-":
        result = int(fNum) - int(sNum)
    elif math == "*":
        result = int(fNum) * int(sNum)
    else:
        result = int(fNum) / int(sNum)

    messagebox.showinfo("Eredmény", str(result))
    fileWrite.writeFile('results.txt', f'művelet: {fNum} {math} {sNum} = {result}')


main = Tk()
main.title('Számológép')
main.geometry('385x400')
main.configure(bg='lightgray')
main.minsize(width=330, height=80)

e = Entry(main, width=20, font=('Arial', 20))
e.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

# Gombok definiálása


btn0 = Button(main, text="0", padx=40, pady=20, command=lambda: btnCl(0))
btn1 = Button(main, text="1", padx=40, pady=20, command=lambda: btnCl(1))
btn2 = Button(main, text="2", padx=40, pady=20, command=lambda: btnCl(2))
btn3 = Button(main, text="3", padx=40, pady=20, command=lambda: btnCl(3))
btn4 = Button(main, text="4", padx=40, pady=20, command=lambda: btnCl(4))
btn5 = Button(main, text="5", padx=40, pady=20, command=lambda: btnCl(5))
btn6 = Button(main, text="6", padx=40, pady=20, command=lambda: btnCl(6))
btn7 = Button(main, text="7", padx=40, pady=20, command=lambda: btnCl(7))
btn8 = Button(main, text="8", padx=40, pady=20, command=lambda: btnCl(8))
btn9 = Button(main, text="9", padx=40, pady=20, command=lambda: btnCl(9))


btnCalc = Button(main, text="=", padx=40, pady=52, command=btnCalculate, bg='#0052cc', fg='#ffffff')
bttnAdd = Button(main, text="+", padx=40, pady=52, command=btnAdd)
bttnSub = Button(main, text="-", padx=40, pady=20, command=btnSub)
bttnDiv = Button(main, text="/", padx=89, pady=20, command=btnDiv)
bttnMulti = Button(main, text="*", padx=89, pady=20, command=btnMulti)
bttnClear = Button(main, text="C", padx=39, pady=20, command=btnClear)

# Gombok elhelíezése

btn9.grid(row=2, column=3)
btn8.grid(row=2, column=2)
btn7.grid(row=2, column=1)
btn6.grid(row=3, column=3)
btn5.grid(row=3, column=2)
btn4.grid(row=3, column=1)
btn3.grid(row=4, column=3)
btn2.grid(row=4, column=2)
btn1.grid(row=4, column=1)
btn0.grid(row=5, column=1)

bttnClear.grid(row=5, column=2)
bttnSub.grid(row=5, column=3)
bttnAdd.grid(row=2, rowspan=2, column=4)
btnCalc.grid(row=4, rowspan=2, column=4)
bttnMulti.grid(row=1, column=1, columnspan=2, )
bttnDiv.grid(row=1, column=3, columnspan=2, )

main.mainloop()
