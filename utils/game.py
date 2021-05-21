""""

Project name : hangman-python

Date of last revision: 20/05/2021

Autor(s) : Vincent Kervyn de Meerendré

Revision N° : Version 1

Client : Becode Bouman3.31

Learning objectives :
    - Learn project architecture
    - Apply basic programming principles (loop, conditions, functions)
    - Reinforce Python syntax

The mission:
    - You will need to create a hangman game in Python, that is played in the terminal.

Project files :
					- utils
					    - game.py
					- main.py
					requirements.txt



"""

################################################
#				Main
################################################

# -----------------------------------------------
#		        Import
# -----------------------------------------------
import random                                #to have random word
import requests                              #to get external online data

# ----------------------------------------------------
#		        Globales
# ----------------------------------------------------


# -------------------------------------------------------
#		        Modules or functions
# -------------------------------------------------------

#

# -------------------------------------------------------
#				PROGRAMME
# -------------------------------------------------------


class Hangman:

    def __init__(self):
        """ Let's built the gallows """

        self.online_words = "https://www.mit.edu/~ecprice/wordlist.10000"
        self.online_list = requests.get(self.online_words)
        self.words = self.online_list.content.splitlines()
        self.possible_words = ['becode', 'learnings', 'mathematics',
                'sessions'] + self.words
        self.word_to_find = random.choice(self.possible_words).decode('utf8').upper()

        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters =  []
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5


    def game_over (self):
        """

        :return:
        """

        print ("Game over. Sorry. ")

    def well_played(self):
        """
        Method used to notify the player that the game is won and how
        :return:
        """
        print(f"Well done! You found the word: {self.word_to_find} in \
                {self.turn_count} turns with {self.error_count} errors!")

    def play (self):
        """

        :return:
        """

        print ("Hangman_the_game")
        allowed_character = 'abcdefghijklmnopqrstuvwxyz'

        already_guessed = []
        self.retry = False
        self.exit = False


        while True:
            self.guess = input("Welcome to my Hangman game! \n" "Please, enter a letter:")
            self.turn_count+=1
            if len(self.guess) != 1:
                print('Please enter a single letter.')
            elif self.guess in already_guessed:
                print('You have already guessed that letter. Choose again.')
            elif self.guess not in allowed_character:
                print('Please enter a LETTER.')
            else:
                return self.guess


            if self.guess in self.word_to_find:
                self.correctly_guessed_letters = self.correctly_guessed_letters + self.guess

                # Check if the player has won.
                found_all_letters = True
                for i in range(len(self.correctly_guessed_letters)):
                    if self.word_to_find[i] not in self.correctly_guessed_letters:
                        found_all_letters = False
                        break
                if found_all_letters:
                   self.well_played()
                   self.game_over = True
            else:
                self.wrongly_guessed_letters = self.wrongly_guessed_letters + self.guess

                # Check if player has guessed too many times and lost.
                if len(self.wrongly_guessed_letters) == self.error_count:
                    self.game_over
                    print('You have run out of guesses!\nAfter ' +
                          str(len(self.error_count)) + ' missed guesses and ' +
                          str(len(self.correctly_guessed_letters)) + ' correct guesses, the word was "' + self.word_to_find + '"')
                    self.game_over = True
                    break

    def start_game(self):
        """

        :return:
        """
        while self.lives > 0:
            self.play(self)
            if self.retry:
                pass
            else: self.exit

