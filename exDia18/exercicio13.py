numeros = []
impares = 0
pares = 0
soma = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
for valor in numeros:
    soma += valor
    

print(f"a soma dos valores é {soma}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")