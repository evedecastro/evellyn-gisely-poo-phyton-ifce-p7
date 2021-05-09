import time

print("-"*40)
time.sleep(1)
print("BEM-VINDE AO DREIECK")
time.sleep(1)
print("aqui você poderá saber o tipo do triângulo sem precisar pensar nisso")
time.sleep(1)
print("-"*40)
time.sleep(0.5)
print("PRECISO QUE DIGITE O TAMANHO DOS LADOS")
time.sleep(1)
print("só os números, sem o tipo de medida")
time.sleep(1)
l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))
print("")
if l1 == l2 == l3:
	print("o seu triangulo é equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
	print("o seu triangulo é isósceles")
else:
	print("o seu triangulo é escaleno")
print("-"*40)
