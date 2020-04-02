# Esse arquivo consiste no jogo "DA FORCA"
# Esse arquivo depende do arquivo externo chamado "listadeanimais.txt"

from random import randint, random
from time import sleep
import emoji

brincar = str(input('QUER BRINCAR COMIGO? S/N: ')).upper()

if brincar == 'S':

    print('{:=^40}'.format(' DÊ START DIGITANDO O NÚMERO DA OPÇÃO: '))
    brincadeira = int(input('''
    [ 1 ] START - JOGO DA FORCA
    '''))

    # =============== BRINCADEIRA 04 ===============
    if brincadeira == 1:
        with open("listadeanimais.txt", "r", encoding="UTF-8") as f:  # Adicionar mais palavras no arquivo
            palavras = f.readlines()
            f.close()
        palavras = [x.rstrip('\n').lower() for x in palavras]
        plv = palavras[int(random() * len(palavras))]
        plv = plv.strip()
        dica = "Animal"
        game = 1
        vidas = 5
        restantes = []
        for x in plv:
            if x != '-' or x != ' ':
                restantes.append("__")
        else:
            restantes.append(x)

        teclas = []
        print("Forca selecionada\n")
        print("!!! LEMBRETE !!!\n Letras com acento estão valendo\n!!! LEMBRETE !!!\n")
        print("\nDica: {}".format(dica))
        print("Vidas restantes: {}".format(vidas))
        while game:
            print("Teclas digitadas {}\n".format(teclas))
            if "".join(restantes) == plv:
                print("\n==========================================")
                print("=============Você GANHOU !! ==============")
                print("==========================================\n")
                break

            if vidas <= 0:
                print("\n!!!!Game Over!!!!\n")
                print("A palavra era '{}'\n".format("".join(plv)))
                break
            print("\t{}".format(restantes))
            tecla = str(input("\nDigite uma tecla >> ")).lower()
            if tecla in teclas:
                print("tecla repetida")
                continue
            if tecla in plv:
                teclas.append(tecla)
                for x in range(0, len(plv)):
                    if tecla == plv[x]:
                        restantes[x] = tecla
            else:
                teclas.append(tecla)
                print("Letra Errada :(")
                vidas = vidas - 1
                print("----> Vidas restantes: {} <----\n".format(vidas))

    else:
        print('Opção inválida!')

else:
    print(emoji.emojize('Tudo bem! Outra hora nós jogamos. :expressionless:', use_aliases=True))

