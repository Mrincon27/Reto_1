def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if primo(num)]
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = [int(num.strip()) for num in entrada.split(",")]

primos = filtrar_primos(numeros)
print(f"Los números primos en la lista {numeros} son: {primos}")
