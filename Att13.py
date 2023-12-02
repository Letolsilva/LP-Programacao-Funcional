def remover_fim(n, lista):
    if n == 0 or n<0 :
        return lista
    elif not lista:
        return []
    else:
        return remover_fim(n - 1, lista[:-1])

print(remover_fim(2, [1, 2, 3, 4, 5, 6]))