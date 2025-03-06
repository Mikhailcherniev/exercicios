while True:
    print("Nova compra iniciada! Insira os valores dos produtos (digite 0 para finalizar a compra).")
    
    total = 0 
    
    while True:
        preco = float(input("Digite o valor do produto (ou 0 para finalizar): "))
        
        if preco == 0:
            break 
        
        if preco < 0:
            print("Valor inválido! Digite um preço positivo.")
        else:
            total += preco  
    print(f"Total da compra: R$ {total:.2f}")
    
    while True:
        pago = float(input("Digite o valor pago pelo cliente: "))
        
        if pago < total:
            print("Valor insuficiente! O cliente deve pagar pelo menos o total da compra.")
        else:
            troco = pago - total
            print(f"Troco: R$ {troco:.2f}")
            break  
    
    print("\nCompra finalizada! Atendendo o próximo cliente...\n")
