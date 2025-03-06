numeros = [] 
contador = 0 
while True:
    num = int(input("Digite um número: "))

    if numeros and num == numeros[-1]:  
        break  

    numeros.append(num) 
    contador += 1  
print(f"Você digitou {contador} números diferentes antes de repetir.")
