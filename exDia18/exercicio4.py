numeros = []
soma = 0 
qtd_numeros = 0

for i in range(5):
    numero = int(input("escreva um numero"))
    numeros.append(numero)
    qtd_numeros += 1 

for valor in numeros:
    soma += valor

media = soma / qtd_numeros

print(f"a soma dos valores é {soma}")
print(f"a media dos valores é {media}")




