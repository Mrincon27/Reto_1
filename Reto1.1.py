def operaciones(N1, N2, operador):

    if operador == "+":
        return N1 + N2
    elif operador == "-":
        return N1 - N2
    elif operador == "*":
        return N1 * N2
    elif operador == "/":
        if N2 == 0:
            return "Error: División por cero." 
        return N1 / N2
    else:
        return "Error: Operador no válido."
    
N1=float(input("ingrese un numero: "))
operador= input("Ingrese el operador (+, -, *, /): ")
N2=float(input("ingrese el segundo numero: "))
resultado=operaciones(N1, N2, operador)
print(f"El resultado de la operacion es: {resultado}")
