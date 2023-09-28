import os
from words import dictionary
from remove_accents import RemoveAccent
from rich import print
from collections import defaultdict


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


    def PrintMatrix(self, matrix):
        for line in matrix:
            word_matrix = "".join(line)
            colors_match = self.CompareWords(word_matrix.lower())
            if not "-" in word_matrix and not " " in word_matrix:
                for idx, char in enumerate(word_matrix):
                    print(f'[{colors_match[idx]}]{char}', end=' ')
                print()
            else:
                print(word_matrix)
        print()
    

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


    def CompareWords(self, word):
        result = ["red"] * 5
        found_letters_counter = defaultdict(int)
        for idx in range(5):
            if word[idx] == self.word[idx]:
                result[idx] = "green"
                found_letters_counter[word[idx]] += 1

        for idx in range(5):
            if word[idx] in self.word and result[idx] != "green":
                if found_letters_counter[word[idx]] < self.word.count(word[idx]):
                    result[idx] = "yellow"
                    found_letters_counter[word[idx]] += 1

        return result


    def RunGame(self):
        self.interface
        while self.current_atmpt <= self.attempts:
            os.system('clear')
            self.PrintMatrix(self.interface)
            # print(self.word)
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
                    self.PrintMatrix(self.interface)    
                    print("[green]Voce[/] venceu!!!")
                    input()
                    break
                else:
                    self.interface[self.current_atmpt] = self.RefreshInterface(self.interface, word_guess)

                self.current_atmpt += 1
            

            else:
                print("Palavra invalida, pressione 'Enter' para tentar novamente")
                input()

                    
        
            
            
            
