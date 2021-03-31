pilha = []
print('Quantos elementos tem a pilha?')
num = int(input())
print('Quais são os elementos?')
for i in range(0, num):
    elemento = input()
    pilha.insert(0, elemento)
print(pilha)
for i in range (0, num):
    print('Clique 1 se deseja retirar um elemento da pilha')
    valor = int(input())
    if valor == 1:
        pilha.pop(0)
        print(pilha)
    else:
        print('O número digitado é inregular')
print("Pilha limpa! Bom trabalho! :)")