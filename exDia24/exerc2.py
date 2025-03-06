num = int(input("Digite um número inteiro positivo: "))


if str(num) == str(num)[::-1]:
    print(f"{num} é um número palíndromo.")
else:
    print(f"{num} não é um número palíndromo.")
