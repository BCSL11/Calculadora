from tkinter import *
window = Tk()
window.title("calculadora")
window.geometry('450x335')
window.resizable(0,0)
aux = 0
input = Entry(window, font=("Arial 20"))

input.grid(row = 0, column =0, columnspan=4, padx=15, pady =10)

button1 = Button(window, text ="1", width=7, height =2, command = lambda: click(1))
button2 = Button(window, text ="2", width=7, height =2, command = lambda: click(2))
button3 = Button(window, text ="3", width=7, height =2, command = lambda: click(3))
button4 = Button(window, text ="4", width=7, height =2, command = lambda: click(4))
button5 = Button(window, text ="5", width=7, height =2, command = lambda: click(5))
button6 = Button(window, text ="6", width=7, height =2, command = lambda: click(6))
button7 = Button(window, text ="7", width=7, height =2, command = lambda: click(7))
button8 = Button(window, text ="8", width=7, height =2, command = lambda: click(8))
button9 = Button(window, text ="9", width=7, height =2, command = lambda: click(9))
button0 = Button(window, text ="0", width=7, height =2, command = lambda: click(0))
buttonDiv = Button(window, text ="/", width=7, height =2, command = lambda: click("/"), state=DISABLED)
buttonMul = Button(window, text ="X", width=7, height =2, command = lambda: click("*"), state=DISABLED)
buttonRes = Button(window, text ="-", width=7, height =2, command = lambda: click("-"), state=DISABLED)
buttonSum = Button(window, text ="+", width=7, height =2, command = lambda: click("+"), state=DISABLED)
buttonP = Button(window, text =".", width=7, height =2, command = lambda: click("."))
buttonDel = Button(window, text ="AC", width=7, height =2, command = lambda:delete())
buttonI = Button(window, text ="=", width=20, height =2, bg='#FBC36A', command= lambda:calculate())

button1.grid(row =4, column=0, padx =10,pady=5)
button2.grid(row =4, column=1, padx =10,pady=5)
button3.grid(row =4, column=2, padx =10,pady=5)
button4.grid(row =3, column=0, padx =10,pady=5)
button5.grid(row =3, column=1, padx =10,pady=5)
button6.grid(row =3, column=2, padx =10,pady=5)
button7.grid(row =2, column=0, padx =10,pady=5)
button8.grid(row =2, column=1, padx =10,pady=5)
button9.grid(row =2, column=2, padx =10,pady=5)
buttonP.grid(row =1, column=2, padx =10,pady=5)
buttonDiv.grid(row =1, column=3, padx =10,pady=5)
buttonMul.grid(row =2, column=3, padx =10,pady=5)
buttonRes.grid(row =3, column=3, padx =10,pady=5)
buttonSum.grid(row =4, column=3, padx =10,pady=5)
button0.grid(row =5, column=1, padx =10,pady=10)
buttonDel.grid(row =5, column=0, padx =10,pady=10)
buttonI.grid(row =5, column=2, columnspan=2, padx =10,pady=10)

def validaCharacterFinal(cadena):
    for i in range(len(cadena)):
        final = cadena[len(cadena)-1]
        return final
   
def calculate():
    calculo = input.get()
    try:
        result= eval(calculo)
        input.delete(0,END)
        input.insert(0,result)
        aux=0
    except:
        input.delete(0,END)
        input.insert(0,"ERROR!!! Fatal :/")
        aux=0


def click(valor):
    global aux
    input.insert(aux, valor)
    aux+=1
    if validaCharacterFinal(input.get()).isdigit() == False:
        buttonMul.config(state=DISABLED)
        buttonDiv.config(state=DISABLED)
        buttonRes.config(state=DISABLED)
        buttonSum.config(state=DISABLED)
        buttonI.config(state=DISABLED)
    else:
        buttonMul.config(state=NORMAL)
        buttonDiv.config(state=NORMAL)
        buttonRes.config(state=NORMAL)
        buttonSum.config(state=NORMAL)
        buttonI.config(state=NORMAL)
  
def delete():
    input.delete(0,END)
    aux=0
    
window.mainloop()