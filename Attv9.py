def palindromo(lista):
    if len(lista) <= 1:
        return True
    else:
        return lista[0] == lista[-1] and palindromo(lista[1:-1])
print(palindromo([1, 2, 3, 4, 3, 2, 1]))
