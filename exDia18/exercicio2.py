numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

inicio = min(numero1, numero2)
fim = max(numero1, numero2)

print(f"Números no intervalo entre {inicio} e {fim}:")
for numero in range(inicio + 1, fim):
    print(numero, end=" ")