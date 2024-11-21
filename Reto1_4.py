def mayor_suma(lista):
    mayor_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual
    
    return mayor_suma
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(num.strip()) for num in entrada.split(",")]

resultado = mayor_suma(numeros)

print(f"La mayor suma de dos números consecutivos en la lista {numeros} es: {resultado}")
