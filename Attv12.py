def muda_esquerda(lista, k):
    if not lista or k >= len(lista):
        return lista

    return lista[k:] + lista[:k]

print(muda_esquerda([1, 5, 6, 7, 3, 4, 1], 3))
