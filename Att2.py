def somaImpares(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somaImpares(list(filter(lambda x: x % 2 != 0, lista[1:])))

print(somaImpares( [1, 3, 2, 7, 4, 6]))
