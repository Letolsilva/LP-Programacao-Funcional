def intercalarLista(lista1, lista2):
    if not lista1:
        return lista2
    elif not lista2:
        return lista1
    elif lista1[0] < lista2[0]:
        return [lista1[0]] + intercalarLista(lista1[1:], lista2)
    else:
        return [lista2[0]] + intercalarLista(lista1, lista2[1:])
print(intercalarLista([1, 5, 10], [2, 7, 9, 20, 25]))
