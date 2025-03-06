notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

digite= int(input("digite uma nota de 0 a 10: "))

while True:
    if digite in notas:
        print("nota valida")

        break
    else:
        print("digite uma nota valida")
        digite = int(input("digite uma nota de 0 a 10: "))