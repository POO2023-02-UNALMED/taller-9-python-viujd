from tkinter import Tk, Button, Entry, END

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x300")

oper=0
i=0

def getNum(n):
    global i
    pantalla.insert(i, n)
    i+=1

def getOper(operador):
    global i, oper
    oper=operador
    pantalla.insert(i, operador)
    i+=1

def calcular():
    global oper
    estado = True
    num1 = ""
    num2 = ""
    estado = pantalla.get()
    pantalla.delete(0, "end")
    for j in estado:
        if(j != oper and estado):
            num1 += j
        elif(j==oper):
            estado = False
        else:
            num2 += j
    
    if(num1 == ""):
        return
    if(num2 == ""):
        return
    if(num1 != "" and num2 != ""):
        for s in num1:
            if(s == "."):
                num1 = float(num1)
                break
        for l in num2:
            if(l == "."):
                num2 = float(num2)
                break
        
        if(type(num1) == str): 
            num1 = int(num1)
            
        if(type(num2) == str): 
            num2 = int(num2)
    
    resultado = 0
    if(oper == "+"):
        resultado = num1 + num2
    elif(oper == "-"):
        resultado = num1 - num2
    elif(oper=="*"):
        resultado = num1 * num2
    elif(oper == "/"):
        resultado = num1 / num2
    
    pantalla.insert(0,resultado)
            


# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=0)

# Configuración botones
boton_1 = Button(root, text="1", command=lambda:getNum(1), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1, sticky="WE")
boton_2 = Button(root, text="2", command=lambda:getNum(2),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1, sticky="WE")
boton_3 = Button(root, text="3", command=lambda:getNum(3),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1, sticky="WE")
boton_4 = Button(root, text="4", command=lambda:getNum(4),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1, sticky="WE")
boton_5 = Button(root, text="5", command=lambda:getNum(5),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1, sticky="WE")
boton_6 = Button(root, text="6", command=lambda:getNum(6),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1, sticky="WE")
boton_7 = Button(root, text="7", command=lambda:getNum(7),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1, sticky="WE")
boton_8 = Button(root, text="8", command=lambda:getNum(8),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1, sticky="WE")
boton_9 = Button(root, text="9", command=lambda:getNum(9),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1, sticky="WE")
boton_igual = Button(root, text="=", command=lambda:calcular(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="WE")
boton_punto = Button(root, text=".", command=lambda:getOper("."),width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1, sticky="WE")
boton_mas = Button(root, text="+", command=lambda:getOper("+"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1, sticky="WE")
boton_menos = Button(root, text="-", command=lambda:getOper("-"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1, sticky="WE")
boton_multiplicacion = Button(root, text="*", command=lambda:getOper("*"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1, sticky="WE")
boton_division = Button(root, text="/",command=lambda:getOper("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1, sticky="WE")

root.mainloop()