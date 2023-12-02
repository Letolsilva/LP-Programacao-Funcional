def distintos(lista):
    if not lista:  # se a lista estiver vazia é pq todos os elementos sao distintos
        return True
    else:
        return not lista[0] in lista[1:] and distintos(lista[1:]) # olha se o primeiro elemento n esta no resto da lista

print(distintos([1, 2, 4, 2, 5]))
print(distintos([3, 2, 1,2])) 