#								Card Fight
#
#	Some license stuff, why not:
#(by default generating, upon creating a file using the IDE 'Geany')
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tum.py tum_classes.py tum_functions.py tum_lists_dicts.py
#  
#  Copyright 2024 Mareyia Z
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
# 							--About the Program--
#
# 'Card Fight' was created for the purpose of completing the 'Portfolio Project: Python Terminal Game' Module
# from CodeCademy: Computer Science Career path.
#
# Before this module there was another project that the course asked of me to create after finishing the
# lessons about Data stractures and Objects in Python3 to test my new skills and it was at that moment that
# I came with the idea of creating the particular program.
#
# At first I was planing to do sepereate projects but after seeing the scale of the project I realized that
# it was more than a simple "test" or a "summary project" and it was fiting for the requirements of the second
# project. 
#
# I progressed and decided to make it as my official portofolio project marking my completion of the
# first section of the Computer Science path.
#
# The project is a small terminal game for two players
# Both players pick a deck with 12 cards each and the are putting the one card against each other. 
#
# The Logic of this game is a simplefied version of the board game "Unmatched":
# "https://en.wikipedia.org/wiki/Unmatched_(board_game)" witch my hole project is based on
#

from cf_list_dicts import instructions
from cf_functions import playGame
from cf_functions import to_continue


# A terminal main menu giving you 3 options and looping on them until you press the exit option that breaks the loop 
menu = None #variable for the selected option, the program just started so the '' corresponds to the choise still hasn't given
#the loop. the option 0 will break the loop aka to exit the game
print("\n=========================================\n========= Welcome to Card fight =========\n=========================================")
while menu!='0':
	print("\n\tMain Menu\n")
	print("Type '1' to start the game,\ntype '2' for instructions\n\nor type '0' to exit\n")
	menu = input("Type here: ")
	
	#safety measure wrong type
	while menu not in ['0', '1', '2']:
		print("--Wrong input--\nTry again:\n\nType '1' to start the game,\ntype '2' for instructions\n\nor type '0' to exit\n".format(menu)) 
		menu = input("Type here: ")
		
	if menu=='2':
		print(instructions)
		to_continue()
	elif menu=='1':
		playGame()
	else:
		print("Bye bye hope you had funnnn, or dont... I actually don't really care.")







































