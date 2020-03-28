
from random import randint,random
from time import sleep
import emoji

brincar = str(input('QUER BRINCAR COMIGO? S/N: ')).upper()

if brincar == 'S':

    print('{:=^40}'.format(' ESCOLHA UMA BRINCADEIRA: '))
    brincadeira = int(input('''
    [ 1 ] ESCONDE-ESCONDE
    [ 2 ] TENTE ADVINHAR
    [ 3 ] JOKENPÔ
    [ 4 ] JOGO DA FORCA
    '''))

    # =============== BRINCADEIRA 01 ===============
    if brincadeira == 1:
        esconderijos = ['Atrás da Arvore', 'No mato do Lote vago',
                        'Embaixo do carro', 'No Beco escuro']
        computador = randint(0, len(esconderijos) - 1)
        print(emoji.emojize(
            'Ok! Você escolheu ESCONDE-ESCONDE. :grinning:', use_aliases=True))
        sleep(2)
        print('3s é o suficiente para eu me esconder, conte até 3 e tente me achar. NÃO VALE OLHAR PRA TRÁS!')
        sleep(2)
        print('Quando você estiver preparado, comece a contar')
        preparado = str(input('Está pronto? S/N: ')).upper()

        if preparado == 'S':
            sleep(1)
            print('UUUuuummmmmmmm 1')
            sleep(1)
            print('DOooisssssssss 2')
            sleep(1)
            print('Treeeeeeiiisss 3')
            sleep(1)
            print('JÁ TO INDO!')

            onde = int(input('''\n Onde estou?
                            [ 1 ] Atrás da Arvore
                            [ 2 ] Mato do Lote vago
                            [ 3 ] Embaixo do carro
                            [ 4 ] Beco escuro
                            '''))-1

            if onde == computador:
                print('Parabéns; você me achou {}'.format(
                    esconderijos[computador]))
            else:
                print('Ops! eu estava escondido {}. Tente outra vez!'.format(
                    esconderijos[computador]))

        elif preparado == 'N':
            print('Tudo bem! Quando estiver preparado, basta dar play no jogo novamente.')
        else:
            print('Opção inválida!')

    # =============== BRINCADEIRA 02 ===============

    elif brincadeira == 2:
        computador = randint(0, 5)
        print(computador)
        print(emoji.emojize(
            'Ok! Você escolheu TENTE ADIVINHAR. :grinning:', use_aliases=True))
        onde = int(input('De 0 a 5, tente adivinhar em qual número eu pensei: '))

        if onde == computador:
            print('Acertou miseravi!')

        elif onde > 5:
            print(
                '\033[31mOPÇÃO INVÁLIDA!\033[m \n Tente um número de 5 pra baixo.')
        else:
            print('Ops! Você errou, eu pensei no número {}'.format(computador))

    # =============== BRINCADEIRA 03 ===============
    elif brincadeira == 3:
        itens = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)
        print(emoji.emojize('Ok! Você escolheu JOKENPÔ. :grinning:', use_aliases=True))
        print(''' Você quer:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA
        ''')

        jogador = int(input('Qual é a sua jogada? '))

        sleep(1)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')

        if computador == 0:
            if jogador == 0:
                print('EMPATOU!')
            elif jogador == 1:
                print('VOCÊ GANHOU! PEDRA PERDE PARA PAPEL.')
            elif jogador == 2:
                print('VOCÊ PERDEU! TESOURA PERDE PARA PEDRA.')
            else:
                print('JOGADA INVÁLIDA!')

        elif computador == 1:
            if jogador == 0:
                print('VOCÊ PERDEU! PEDRA PERDE PARA PAPEL.')
            elif jogador == 1:
                print('EMPATOU!')
            elif jogador == 2:
                print('VOCÊ GANHOU! PAPEL PERDE PARA TESOURA.')
            else:
                print('JOGADA INVÁLIDA!')

        elif computador == 2:
            if jogador == 0:
                print('VOCÊ GANHOU! TESOURA PERDE PARA PEDRA.')
            elif jogador == 1:
                print('VOCÊ PERDEU! PAPEL PERDE PARA TESOURA.')
            elif jogador == 2:
                print('EMPATOU!')
            else:
                print('JOGADA INVÁLIDA!')
    # =============== BRINCADEIRA 04 ===============
    elif brincadeira == 4:
        # forca
        with open("listadeanimais.txt","r",encoding="UTF-8") as f: #Adicionar mais palavras no arquivo
            palavras = f.readlines()
            f.close()
        palavras = [x.rstrip('\n').lower() for x in palavras]
        plv = palavras[int(random()*len(palavras))]
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
                for x in range(0,len(plv)):
                    if tecla == plv[x]:
                        restantes[x] = tecla
            else:
                teclas.append(tecla)
                print("Letra Errada :(")
                vidas = vidas - 1
                print("----> Vidas restantes: {} <----\n".format(vidas))



    

else:
    print(emoji.emojize(
        'Tudo bem! Outra hora nós jogamos. :expressionless:', use_aliases=True))

