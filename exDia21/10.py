
votos = {
    1: {"nome": "bolsonaro", "quantidade": 0},
    2: {"nome": "lula", "quantidade": 0},
    3: {"nome": "tabata", "quantidade": 0},
    4: {"nome": "candidato padre", "quantidade": 0},
    5: {"nome": "Voto Nulo", "quantidade": 0},
    6: {"nome": "Voto Branco", "quantidade": 0}
}

total_votos = 0  

print("=== SISTEMA DE VOTAÇÃO ===")
print("\nCandidatos disponíveis:")
for codigo, info in votos.items():
    print(f"{codigo} - {info['nome']}")

print("\nDigite o número do candidato para votar, 5 para nulo, 6 para branco ou 0 para encerrar.")


while True:
    voto = int(input("\nSeu voto: "))

    if voto == 0:
        break 

    if voto in votos:
        votos[voto]["quantidade"] += 1
        total_votos += 1
        print(f"Voto registrado para {votos[voto]['nome']}.")
    else:
        print("Opção inválida! Digite um número válido.")


print("\n=== RESULTADO DA VOTAÇÃO ===")
for codigo, info in votos.items():
    print(f"{info['nome']}: {info['quantidade']} votos")


if total_votos > 0:
    votos_nulos = votos[5]["quantidade"]
    votos_brancos = votos[6]["quantidade"]

    percentual_nulos = (votos_nulos / total_votos) * 100
    percentual_brancos = (votos_brancos / total_votos) * 100

    print(f"\nPorcentagem de votos nulos: {percentual_nulos:.2f}%")
    print(f"Porcentagem de votos brancos: {percentual_brancos:.2f}%")
else:
    print("\nNenhum voto registrado.")

print("\nVotação encerrada!")
