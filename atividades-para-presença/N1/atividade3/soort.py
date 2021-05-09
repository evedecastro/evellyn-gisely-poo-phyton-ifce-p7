import random
import time

print("-"*30)
time.sleep(1)
print("BEM-VINDE AO SOORT!!")
time.sleep(1)
print("QUER APOSTAR NA MEGA MAS NÃO SABE QUE NÚMERO ESCOLHER?")
time.sleep(1)
print("O SOORT SOLUCIONA ESSE PROBLEMA PARA VOCÊ")
print("-"*30)
time.sleep(1)

def existeNumero(numeros, n): 
    return n in numeros


x = input("CLIQUE 1 PARA SORTEAR: ")
resultado = []
if x == '1':
	for i in range (0,5):
		sorteado = (random.randrange(1, 61))
		resultado.append(sorteado)
	time.sleep(1)
	print("")
	print ("SEUS NÚMEROS DE APOSTA SÃO:\n", resultado)
	print("-"*30)
