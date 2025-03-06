num = int(input("digite um numero"))
contadorePares = 0

while num != -1:
    if num %2 == 0:
          print ("voce digitou um numero par")
          contadorePares += 1
    num = int(input("digite um numero ou digite -1 para parar"))
print(f"o numeros de numeros pare é:{contadorePares}")