fila = []
print('Quantos elementos tem a fila?')
num = int(input())
print('Quais são os elementos?')
for i in range(0, num):
    elemento = input()
    fila.append(elemento)
print(fila)
for i in range (0, num):
    print('Clique 1 se deseja retirar um elemento da fila')
    valor = int(input())
    if valor == 1:
        fila.pop(0)
        print(fila)
    else:
        print('O número digitado é inregular')
print("Fila vazia! Bom trabalho! :)")