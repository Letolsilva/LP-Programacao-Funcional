def primo(numero, divisor=None):
    # Caso 1: números menores que 2 não são primos
    if numero < 2:
        return False
    # Caso 2: se chegamos a 2, é primo
    elif numero == 2:
        return True
    # Caso 3: se o número é divisível por algum número até sua raiz quadrada, não é primo
    elif divisor is not None and divisor > numero ** 0.5:
        return True
    # Caso 4: verificar se o número é divisível pelo divisor atual
    elif divisor is not None and numero % divisor == 0:
        return False
    else:
        return primo(numero, divisor + 1) if divisor is not None else primo(numero, 2)

print(primo(12))  
print(primo(17))   
