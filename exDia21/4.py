maior = None 

while True:
    num = float(input("Digite um número (ou um número negativo para sair): "))

    if num < 0:
        break  

    if maior is None or num > maior:
        maior = num  

if maior is not None:
    print(f"O maior número informado foi: {maior}")
else:
    print("Nenhum número positivo foi inserido.")
