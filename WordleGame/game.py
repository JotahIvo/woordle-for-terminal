import os
from words import dictionary
from remove_accents import RemoveAccent
from rich import print


class Wordle:
    def __init__(self, word, aWord):
        self.word = word
        self.aWord = aWord
        self.attempts = 6
        self.current_atmpt = 0 
        self.interface = [['-','-','-','-','-'],
                          ['-','-','-','-','-'],
                          ['-','-','-','-','-'],
                          ['-','-','-','-','-'],
                          ['-','-','-','-','-'],
                          ['-','-','-','-','-'], 
                        ]


    def PrintMatrix(self, matrix, word):
        for l in matrix:
            line = " ".join(l)
            idx = 0
            for char in line:
                if char != ' ' and char != '-' and idx < 6:
                    if self.PaintLetters(char.lower(), idx, word.lower()) == 'green':
                        print(f'[green]{char}', end='')
                        idx += 1
                    elif self.PaintLetters(char.lower(), idx, word.lower()) == 'yellow':
                        print(f'[yellow]{char}', end='')
                        idx += 1
                    else:
                        print(f'[red]{char}', end='')
                        idx += 1
                else:
                    print(char, end='')
            print('\n')
    

    def RefreshInterface(self, interface, word):
        list = []
        word = word.upper()
        for char in word:
            list.append(char)
        
        return list
    

    def ValidateWord(self, word):
        if word in dictionary and len(word) == 5:
            return True
        else:
            return False


    def CheckWin(self, tryWord):
        if self.word == tryWord or self.aWord == tryWord:
            return True
        else:
            return False


    def PaintLetters(self, char, position, _word):
        nChar = self.word.count(char)
        newString = _word[0:position+1]
        nCharInNS = newString.count(char)

        if char.lower() == self.word[position]:
            return 'green'
        elif char.lower() in self.word and nCharInNS <= nChar:
            return 'yellow'
        else:
            return 'red'


    def RunGame(self):
        self.interface
        while self.current_atmpt <= self.attempts:
            os.system('clear')
            self.PrintMatrix(self.interface, '')
            #print(self.word)
            print(f'Voce tem {self.attempts - self.current_atmpt} tentativas restantes')

            if self.attempts - self.current_atmpt == 0:
                print(f'Voce [red]perdeu!!![/]\nA palavra era [red]{self.aWord}[/]')
                input("\nPressione 'Enter' para continuar:")
                break

            word_guess = str(input("Digite a palavra: "))
            word_guess = RemoveAccent(word_guess).lower()

            if self.ValidateWord(word_guess):
                if self.CheckWin(word_guess):
                    os.system('clear')
                    self.interface[self.current_atmpt] = self.RefreshInterface(self.interface, word_guess)
                    self.PrintMatrix(self.interface, word_guess.lower())
                    print("[green]Voce[/] venceu!!!")
                    input()
                    break
                else:
                    self.interface[self.current_atmpt] = self.RefreshInterface(self.interface, word_guess)

                self.current_atmpt += 1
            

            else:
                print("Palavra invalida, pressione 'Enter' para tentar novamente")
                input()

                    
        
            
            
            
