lista = []
print('Quantos elementos tem a lista?')
num = int(input())
for i in range(0, num):
    print('Onde você quer inserir o elemento?')
    lugar = int(input())
    print('Que elemento você quer inserir?')
    elemento = input()
    lista.insert(lugar, elemento)
print(lista)
for i in range(0, num):
    print('Qual elemento deseja retirar da lista?')
    remover = input()
    lista.remove(remover)
    print(lista)
print("Fim da lista! Bom trabalho! :)")