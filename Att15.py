def trocar(valor):
    if valor <= 0:
        return []
    elif valor >= 100:
        return [100] + trocar(valor - 100)
    elif valor >= 50:
        return [50] + trocar(valor - 50)
    elif valor >= 10:
        return [10] + trocar(valor - 10)
    elif valor >= 5:
        return [5] + trocar(valor - 5)
    else:
        return [1] + trocar(valor - 1)

print(sorted(trocar(162)))
