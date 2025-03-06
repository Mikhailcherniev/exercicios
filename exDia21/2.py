senha = "1234"
tentativa = input("digite a senha: ")

while tentativa != senha:
    print("senha incorreta, tente novamente:")
    tentativa = input("digite a senha")

print("senha correta")