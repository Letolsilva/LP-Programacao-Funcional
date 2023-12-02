def disjuntas(lista1, lista2):
    # Caso 1: uma das listas é vazia
    if not lista1:
        return True
    elif not lista2:
        return True
    # Caso 2: o primeiro elemento de uma lista está na outra
    elif lista1[0] in lista2 or lista2[0] in lista1:
        return False
    # comparar os primeiros elementos e chamar recursivamente
    else:
        return disjuntas(lista1[1:], lista2) and disjuntas(lista1, lista2[1:])

print(disjuntas([1, 2, 3],  [5, 4, 6, 0]))
