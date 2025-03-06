print("Valor da Compra - Desconto - Valor Final")

valor_compra = int(input("Digite o valor da compra: "))

desconto = min((valor_compra // 100) - 4, 25) 
valor_final = valor_compra - (valor_compra * desconto / 100) 
print(f"R${valor_compra},00 - {desconto}% - R${valor_final:.2f}")
