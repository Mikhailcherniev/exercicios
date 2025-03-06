
produtos = {
    1: {"nome": "Camiseta", "preco": 25.00},
    2: {"nome": "Calça", "preco": 50.00},
    3: {"nome": "Tênis", "preco": 120.00},
    4: {"nome": "Boné", "preco": 30.00},
    5: {"nome": "Meia", "preco": 10.00}
}

while True:
    print("Lista de produtos disponíveis:")
    for codigo, info in produtos.items():
        print(f"{codigo} - {info['nome']} - R$ {info['preco']:.2f}")
    
    total = 0  
    
    while True:
        codigo = int(input("Digite o código do produto (ou 0 para finalizar): "))
        
        if codigo == 0:
            break 

        if codigo not in produtos:
            print("Código inválido! Digite um código válido.")
            continue
        
        quantidade = int(input(f"Digite a quantidade de {produtos[codigo]['nome']}: "))
        
        if quantidade <= 0:
            print("Quantidade inválida! Insira um valor maior que zero.")
            continue
        
        total += produtos[codigo]['preco'] * quantidade 
        print(f"Item adicionado: {quantidade}x {produtos[codigo]['nome']}")

    print(f"Total do pedido: R$ {total:.2f}")
    
    while True:
        pago = float(input("Digite o valor pago pelo cliente: "))
        
        if pago < total:
            print("Valor insuficiente! O cliente deve pagar pelo menos o total da compra.")
        else:
            troco = pago - total
            print(f"Troco: R$ {troco:.2f}")
            break  
    
    print("Pedido finalizado! Atendendo o próximo cliente...")
