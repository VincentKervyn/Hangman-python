"""

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
from utils.game import Hangman

game1 = Hangman()
game1.start_game()



