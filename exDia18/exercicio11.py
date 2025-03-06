turma = []
soma = 0

faixa = int(input("Insira a quantidade de pessoas na turma: "))

for i in range(faixa):
    idade = int(input(f"Insira a idade da {i}° pessoa: "))
    soma += idade
media = soma / faixa

if media <= 25:
    print("jovem")
elif 26 <= media <= 60:
    print("adulta") 
else:
    print("idosa")