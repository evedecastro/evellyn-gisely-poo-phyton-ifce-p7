import time

x = False
def TRIÂNGULO():
	if a or b or c == 0:
		x = False
	elif (b - c) < a < b + c:
		x = True
	elif (a - c) < b < a + c:
		x = True
	elif (a - b) < c < a + b:
		x = True
		

print("-"*40)
time.sleep(1)
print("QUER SABER SE CONSEGUE CONSTRUIR UM TRIÂNGULO COM ESSES CANUDOS?")
time.sleep(1)
print("ENTÃO VEM COMIGO QUE EU TE AJUDO!")
time.sleep(1)
print("-"*40)
time.sleep(1)
print("AGORA DIGITE O TAMANHO DOS CANUDOS:")
time.sleep(1)
a = int(input("Canudo 1: "))
b = int(input("Canudo 2: "))
c = int(input("Canudo 3: "))
TRIÂNGULO()
print("")
time.sleep(1)
if x == True:
	print("EBAAA! ELES FORMAM UM TRIÂNGULO :)")
else:
	print("POXA :( ELES NÃO FORMAM UM TRIÂNGULO")
print("-"*40)
