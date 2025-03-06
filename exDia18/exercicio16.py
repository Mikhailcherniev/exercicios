faixas = {
    "Até 15 anos": 0,
    "De 16 a 30 anos": 0,
    "De 31 a 45 anos": 0,
    "De 46 a 60 anos": 0,
    "Acima de 61 anos": 0
}

total_pessoas = 15

for i in range(total_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    if idade <= 15:
        faixas["Até 15 anos"] += 1
    elif 16 <= idade <= 30:
        faixas["De 16 a 30 anos"] += 1
    elif 31 <= idade <= 45:
        faixas["De 31 a 45 anos"] += 1
    elif 46 <= idade <= 60:
        faixas["De 46 a 60 anos"] += 1
    else:
        faixas["Acima de 61 anos"] += 1

print("\nQuantidade de pessoas em cada faixa etária:")
for faixa, quantidade in faixas.items():
    print(f"{faixa}: {quantidade}")

percentagem_primeira = (faixas["Até 15 anos"] / total_pessoas) * 100
percentagem_ultima = (faixas["Acima de 61 anos"] / total_pessoas) * 100

print(f"\nPercentagem de pessoas até 15 anos: {percentagem_primeira:.2f}%")
print(f"Percentagem de pessoas acima de 61 anos: {percentagem_ultima:.2f}%")