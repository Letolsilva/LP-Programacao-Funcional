def substituirElementos(lista, Inteiro, NovoInteiro):
    return list(map(lambda x: NovoInteiro if x == Inteiro else x, lista))

print(substituirElementos([1, 2, 1, 3, 1], 1, 0))
