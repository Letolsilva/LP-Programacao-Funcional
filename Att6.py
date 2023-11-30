def eh_perfeito(numero, divisor=1, soma=0):
    # Caso base: número menor que 2 não é perfeito
    if numero < 2:
        return False
    # Caso base: soma dos divisores igual ao número
    elif divisor > numero / 2:
        return soma == numero
    # Caso recursivo: verificar se o número é divisível pelo divisor atual
    elif numero % divisor == 0:
        return eh_perfeito(numero, divisor + 1, soma + divisor)
    # Caso recursivo: chamar a função recursivamente com o próximo divisor
    else:
        return eh_perfeito(numero, divisor + 1, soma)

# Exemplo de uso
print(eh_perfeito(28))  # True
