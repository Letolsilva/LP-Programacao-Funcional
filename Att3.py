def substituir_elementos(lista, Inteiro, NovoInteiro):
    return list(map(lambda x: NovoInteiro if x == Inteiro else x, lista))

print(substituir_elementos([1, 2, 1, 3, 1], 1, 0))
