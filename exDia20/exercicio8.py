maior = None  
num = int(input("Digite um número (ou 0 para parar): "))

while num != 0:  
    if maior is None or num > maior:  
        maior = num  
    
    num = int(input("Digite outro número (ou 0 para parar): "))  

if maior is not None:
    print(f"O maior número inserido foi: {maior}")
else:
    print("Nenhum número foi inserido.")
