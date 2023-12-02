def linearizar(lista_de_listas):
    if not lista_de_listas:
        return []
    else:
        return lista_de_listas[0] + linearizar(lista_de_listas[1:])
print(linearizar( [[1, 2], [5], [0, 4, 2]]))
