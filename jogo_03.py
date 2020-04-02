# Esse arquivo consiste no jogo "JOKENPÔ"

from random import randint, random
from time import sleep
import emoji

brincar = str(input('QUER BRINCAR COMIGO? S/N: ')).upper()

if brincar == 'S':

    print('{:=^40}'.format(' DÊ START DIGITANDO O NÚMERO DA OPÇÃO: '))
    brincadeira = int(input('''
    [ 1 ] START - JOKENPÔ
    '''))

        # =============== BRINCADEIRA 03 ===============
    if brincadeira == 1:
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
                print('JOGADA INVÁLIDAAAAA!')

        elif computador == 2:
            if jogador == 0:
                print('VOCÊ GANHOU! TESOURA PERDE PARA PEDRA.')
            elif jogador == 1:
                print('VOCÊ PERDEU! PAPEL PERDE PARA TESOURA.')
            elif jogador == 2:
                print('EMPATOU!')
            else:
                print('JOGADA INVÁLIDA!')

    else:
        print('Opção inválida!')


else:
    print(emoji.emojize('Tudo bem! Outra hora nós jogamos. :expressionless:', use_aliases=True))

