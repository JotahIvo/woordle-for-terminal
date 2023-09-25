from words import dictionary
import random
import os, sys
from rich import print
from game import Wordle

os.system('clear')

while True:
    os.system('clear')
    print('''
WORDLE:

[1] - Digite 1 para aprender a jogar
[2] - Digite 2 para jogar Wordle
[3] - Digite 3 para sair do jogo
''')

    option = str(input('Escolha uma opção: '))

    match option:
        case '1':
            os.system('clear')
            print('[green]COMO JOGAR?[/]')
            print('\n> Voce possui 6 tentativas para acertar a palavra de 5 letras.')
            print('> Somente palavras existentes e de 5 letras serao aceitas como input')
            print('\n> Caso a letra fique [red]vermelha[/] significa que nao existe essa letra na palavra')
            print('> Caso a letra fique [yellow]amarela[/] a letra existe na palavra mas esta na posiçao errada.')
            print('> Caso a letra fique [green]verde[/] a letra existe e esta na posiç~ao certa na palavra.')
            input("\nPressione 'Enter' para continuar:")

        case '2':
            os.system('clear')
            word, aWord = random.choice(list(dictionary.items())) 
            """ word = 'anel'
            aWord = 'anel' """
            print('WORDLE')
            wordle = Wordle(word, aWord)
            wordle.RunGame()

        case '3':
            print('Obrigado por jogar Wordle For Terminal!!!')
            sys.exit()
    