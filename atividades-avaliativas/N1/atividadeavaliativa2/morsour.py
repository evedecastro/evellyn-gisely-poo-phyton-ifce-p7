from time import sleep

print("〰"*25)
print("Bem vindo ao Morsour")
print("Seu tradutor de texto para código Morse")
print("〰"*25)

traducao = {'B': '-...',    'A': '.-',   'C': '-.-.',    'D': '-..',
       'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
       'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
       'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
       'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
       'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
       'Y': '-.--', 'Z': '--..',

       '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
       '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
       '8': '---..',    '9': '----.',   ' ': ' '
        }
option = '1'

while option == '1':
    try:
        text = input('Digite aqui o texto: ').upper()

        morse = ''

        for char in text:
            sleep(1)
            morse = traducao[char]
            if char != " ":
                print("{}".format(morse))
            else:
                print(morse)

        sleep(1)

		
        print('Sua tradução foi finalizada')
        print("〰"*25)

        sleep(1)
        print("Deseja traduzir outro texto?")
        option = input("1. Sim\n2. Não\n=> ")
        print("〰"*25)
        
    except KeyError as e:
        char_error = str(e).replace("\'", '')
        print('{} = Caractere não reconhecido'.format(char_error))
        print('Tente novamente!')
    except KeyboardInterrupt:
        option = '2'
        print('')

print("Eu vou sentir saudades 😫")
print("Volte quando quiser 🙃")
print("〰"*25)
