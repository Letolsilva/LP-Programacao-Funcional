def numPerfeito(numero, divisor=1, soma=0):
    # Caso 1: número menor que 2 não é perfeito
    if numero < 2:
        return False
    # Caso 2: soma dos divisores igual ao número
    elif divisor > numero / 2:
        return soma == numero
    # Caso 3: verificar se o número é divisível pelo divisor atual
    elif numero % divisor == 0:
        return numPerfeito(numero, divisor + 1, soma + divisor)
    else:
        return numPerfeito(numero, divisor + 1, soma)

print(numPerfeito(28)) 
