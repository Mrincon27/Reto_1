def palindromo(palabra):
    palabra = palabra.lower()
    longitud_p = len(palabra)

    for i in range(longitud_p // 2):
        if palabra[i] != palabra[longitud_p - 1 - i]:
            return False
    return True

palabra = input("Ingrese una palabra para verificar si es palíndromo: ")

es_palindromo = palindromo(palabra)
print(f"La palabra '{palabra}' {'es' if es_palindromo else 'no es'} un palíndromo.")
