def soma_impares_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_impares_recursiva(list(filter(lambda x: x % 2 != 0, lista[1:])))

print(soma_impares_recursiva( [1, 3, 2, 7, 4, 6]))
