cliente = []

for i in range(5):
    nome = input('Insira o nome do cliente: ')
    cliente.append(nome)

faturamentoA = int(input('Insira o faturamento da loja A: '))

if faturamentoA >+ 54000:
    print(f"O faturamento foi superado em {faturamentoA - 54000}")

