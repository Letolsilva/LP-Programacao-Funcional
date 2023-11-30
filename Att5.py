def binario(numero):
    if numero == 0:
        return [0]
    elif numero == 1:
        return [1]
    else:
        return binario(numero // 2) + [numero % 2] # // retorna o quociente

print(binario(8))
