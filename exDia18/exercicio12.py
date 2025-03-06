listaCandidato = []
numeroVotos = 0  
votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0

numeroEleitores = int(input("Digite o número total de eleitores: "))


for i in range(3):
    candidato = input(f"Digite o nome do candidato {i + 1}: ")
    listaCandidato.append(candidato)


for i in range(numeroEleitores):
    print(f"Eleitor {i + 1}, vote em um dos candidatos:")
    
   
    contador = 1
    for candidato in listaCandidato:
        print(f"{contador}. {candidato}")
        contador += 1  
    voto = int(input("Digite o número do seu candidato: "))

    if voto == 1:
        votosCandidato1 += 1
    elif voto == 2:
        votosCandidato2 += 1
    elif voto == 3:
        votosCandidato3 += 1
    else:
        print("Voto inválido. Por favor, vote novamente.")
        i -= 1 

print("Resultados da eleição:")


print(f"{listaCandidato[0]}: {votosCandidato1} votos")
print(f"{listaCandidato[1]}: {votosCandidato2} votos")
print(f"{listaCandidato[2]}: {votosCandidato3} votos")