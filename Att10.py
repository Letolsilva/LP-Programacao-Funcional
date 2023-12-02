def somas_parciais(lista):
    if not lista:
        return []
    else:
        return somas_parciais(lista[:-1]) + [sum(lista)]

print(somas_parciais([1,2,3,4]))