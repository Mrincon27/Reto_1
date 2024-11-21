def anagramas(lista):
    lista1 = {}
    for palabra in lista:
        clave = ''.join(sorted(palabra))
        if clave in lista1:
            lista1[clave].append(palabra)
        else:
            lista1[clave] = [palabra]
    resultado = []
    for grupo in lista1.values():
        if len(grupo) > 1:
            resultado.extend(grupo)
    
    return resultado

entrada = ["amor","roma","mora","corazon","razonar"]
salida = anagramas(entrada)
print(salida)