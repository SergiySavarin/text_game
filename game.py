#! /usr/bin/env python

import os
import random
import sys
from sys import stdout
from time import sleep
from termcolor import colored

def eating(ran_n):
	for i in range(0, ran_n):
		s1 = colored('~o:<', 'red') + (colored('~', 'green') * (ran_n - i)) + (' ' * i)
		stdout.write('\r')
		stdout.write(s1)
		stdout.flush()
		sleep(0.2)
		s2 = colored('-o:> ', 'red') + (colored('~', 'green') * ((ran_n - 1) - i)) + (' ' * i)
		stdout.write('\r')
		stdout.write(s2)
		stdout.flush()
		sleep(0.2)
	print '\n'

def killing(ran_n, num):
	for i in range(0, ran_n):
		if i == num:
			choice_point()
			print colored('~o:<', 'red') + (' ' * (ran_n - 4)) + colored('<:o-', 'red'), '\n'
			inpt = raw_input('>')

			if inpt == '1':
				os.system('clear')
				for i in range(0, ran_n):
					s1 = colored('<:o~', 'red') + (' ' * ((ran_n - 6) - i)) + colored('<-' 'magenta') + (' ' * i) + colored('<:o-', 'red')
					stdout.write('\r')
					stdout.write(s1)
					stdout.flush()
					sleep(0.2)			
					s2 = colored('<:o-', 'red') + (' ' * ((ran_n - 7) - i)) + colored('<-' 'magenta') + (' ' * i) + colored('>:o~', 'red')
					stdout.write('\r')
					stdout.write(s2)
					stdout.flush()
					sleep(0.2)
				os.system('clear')
				print '\n'

			if inpt == '2':
				os.system('clear')
				for i in range(0, ran_n):
					s1 = colored('<:o~', 'red') + (' ' * ((ran_n - 4) - i)) + colored('<:o-', 'red') + (' ' * i)
					stdout.write('\r')
					stdout.write(s1)
					stdout.flush()
					sleep(0.2)			
					s2 = colored('<:o-', 'red') + (' ' * ((ran_n - 5) - i)) + colored('>:o-', 'red') + (' ' * i)
					stdout.write('\r')
					stdout.write(s2)
					stdout.flush()
					sleep(0.2)
				os.system('clear')
				print '\n'
		else:
			s1 = '~o:<' + ('~' * (ran_n - i)) + (' ' * i)
			stdout.write('\r')
			stdout.write(s1)
			stdout.flush()
			sleep(0.2)
			s2 = '-o:> ' + ('~' * ((ran_n - 1) - i)) + (' ' * i)
			stdout.write('\r')
			stdout.write(s2)
			stdout.flush()
			sleep(0.2)
	print '\n'
	return inpt

def choice_point():
	print '\n',\
		  '/----------------------------------------\ ', '\n',\
    	  '|  You met a member from nearest colony  |', '\n',\
		  '|             `Eubacteries`              |', '\n',\
		  '|                                        |', '\n',\
		  '|      What are you decide to do?        |', '\n',\
		  '|        Press 1 to kill him             |', '\n',\
		  '|        Press 2 to eat him              |', '\n',\
		  '|        Press 3 to stole his area       |', '\n',\
		  '|        Press 4 to do nothing           |', '\n',\
    	  '\----------------------------------------/', '\n'


os.system('clear')

print colored('/----------------------------------------\ ', 'blue'), '\n',\
      colored('| And was decided, and Earth was created.|', 'blue'), '\n',\
      colored('\----------------------------------------/', 'blue')
print '/----------------------------------------\ ', '\n',\
      '| Hi there, it`s time more than 4000 ml  |', '\n',\
      '|     years ago, when was no life,       |', '\n',\
      '|    but something start to evolve.      |', '\n',\
      '| If you want evolve Life in the Earth   |', '\n', \
      '|             just tap `c`.              |', '\n',\
      '\----------------------------------------/'

a = raw_input('>').lower()

if a == 'c':
	os.system('clear')
	for i in range(0, 101, 1):
		k = i / 4
		stdout.write('\r')
		stdout.write('Creating Life:')
		stdout.write(colored('=', 'blue') * k)
		stdout.write(colored('>%d', 'blue') % i)
		stdout.write(colored('%', 'blue'))
		stdout.flush()
		sleep(0.1)
	stdout.write('\n')
	print '/----------------------------------------\ ', '\n',\
	      '| Nice it`s already passed 1000 mln.yrs.,|', '\n',\
	      '|       and first life was created.      |', '\n',\
	      '\----------------------------------------/'
	print '/----------------------------------------\`', '\n',\
		  '|         My congratulations!            |', '\n',\
		  '|        Your name is `Bacteria`.        |', '\n',\
		  '|          Let`s start evolve.           |', '\n',\
		  '|    Maybe you`ll become Homosapiens.    |', '\n',\
		  '\----------------------------------------/'
	choice = True
else:
	os.system('clear')
	print '/----------------------------------------\ ', '\n',\
    	  '|          Great. See you later.         |', '\n',\
    	  '\----------------------------------------/'

while choice == True:
	print '/----------------------------------------\ ', '\n',\
	      '|     You have few choices what to do    |', '\n',\
	      '|    to be alive. To eat and multiply.   |', '\n',\
	      '|  If you want use it, just tap `enter`. |', '\n',\
	      '\----------------------------------------/'
	ran_n = random.randint(25, 39)
	raw_input()
	eating(ran_n)
	os.system('clear')
	print '/----------------------------------------\ ', '\n',\
	      '| Great it`s already passed 2500 mln.yrs.|', '\n',\
		  '|    You ate enough, and now you are     |', '\n',\
		  '|  so powerfull that you can evolve to   |', '\n',\
		  '| `Arhaea`, `Eukariotes` or `Eubacteria`.|', '\n',\
		  '|                                        |', '\n',\
		  '|           Make your choice:            |', '\n',\
		  '|     Press 1 to choose `Arhaea`         |', '\n',\
		  '|     Press 2 to choose `Eukariotes`     |', '\n',\
		  '|     Press 3 to choose `Eubacteria`     |', '\n',\
		  '|                                        |', '\n',\
		  '|   And rememder everything depend on    |', '\n',\
		  '|              Your Choice!              |', '\n',\
	      '\----------------------------------------/'
	inpt = raw_input('>')
	if inpt == '1':
		os.system('clear')
		print '/----------------------------------------\ ', '\n',\
	    	  '| Great.You can eat and multiply so mach |', '\n',\
			  '|  as you want. And you`ll be seen with  |', '\n',\
			  '|  the humans, when they discovered you  |', '\n',\
			  '|           after 1500 ml.yrs.           |', '\n',\
			  '|                                        |', '\n',\
			  '|                 BYE                    |', '\n',\
			  '|                                        |', '\n',\
	    	  '\----------------------------------------/'
		choice = False
	elif inpt == '2':
		os.system('clear')
		print '/----------------------------------------\ ', '\n',\
			  '|         My congratulations!            |', '\n',\
			  '|        Let`s evolve further.           |', '\n',\
			  '|    Maybe you`ll become Homosapiens.    |', '\n',\
			  '|                                        |', '\n',\
		      '|     As always you have few choices     |', '\n',\
		      '|     to evolve. To eat and multiply.    |', '\n',\
		      '|  If you want use it, just tap `enter`. |', '\n',\
			  '\----------------------------------------/'
		ran_n = random.randint(25, 39)
		raw_input()
		skill = killing(ran_n, 20)
		os.system('clear')
		print '/----------------------------------------\ ', '\n',\
		      '| Great it`s already passed 2500 mln.yrs.|', '\n',\
			  '|    You ate enough, and now you are     |', '\n',\
			  '|  so powerfull that you can evolve to   |', '\n',\
			  '|      `Green Plants`, `Oar weed` or     |', '\n',\
			  '|             `Opisthokonts`             |', '\n',\
			  '|                                        |', '\n',\
			  '|           Make your choice:            |', '\n',\
			  '|     Press 1 to choose `Green Plants`   |', '\n',\
			  '|     Press 2 to choose `Oar weed`       |', '\n',\
			  '|     Press 3 to choose `Opisthokonts`   |', '\n',\
			  '|                                        |', '\n',\
			  '|   And rememder everything depend on    |', '\n',\
			  '|              Your Choice!              |', '\n',\
		      '\----------------------------------------/'

		inpt = raw_input('>')

		if inpt == '1' and (skill == '3' or skill == '1'):

			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
				  '|         My congratulations!            |', '\n',\
				  '|        Let`s evolve further.           |', '\n',\
				  '|    Maybe you`ll become Homosapiens.    |', '\n',\
				  '|                                        |', '\n',\
			      '|     As always you have few choices     |', '\n',\
			      '|     to evolve. To eat and multiply.    |', '\n',\
			      '|  If you want use it, just tap `enter`. |', '\n',\
				  '\----------------------------------------/'
			ran_n = random.randint(25, 39)
			raw_input()
			skill = killing(ran_n, 20)
			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
			      '| Great it`s already passed 2500 mln.yrs.|', '\n',\
				  '|    You ate enough, and now you are     |', '\n',\
				  '|  so powerfull that you can evolve to   |', '\n',\
				  '|      `Green Algae`, `Land plants`      |', '\n',\
				  '|                                        |', '\n',\
				  '|           Make your choice:            |', '\n',\
				  '|     Press 1 to choose `Green Algae`    |', '\n',\
				  '|     Press 2 to choose `Land plants`    |', '\n',\
				  '|                                        |', '\n',\
				  '|   And rememder everything depend on    |', '\n',\
				  '|              Your Choice!              |', '\n',\
			      '\----------------------------------------/'
			inpt = raw_input('>')
			if inpt == '1':
				os.system('clear')
				print '/----------------------------------------\ ', '\n',\
			    	  '| Great.You can eat and multiply so mach |', '\n',\
					  '|  as you want. And you`ll be seen with  |', '\n',\
					  '|  the humans, when they discovered you  |', '\n',\
					  '|           after 1000 ml.yrs.           |', '\n',\
					  '|                                        |', '\n',\
					  '|                 BYE                    |', '\n',\
					  '|                                        |', '\n',\
			    	  '\----------------------------------------/'
				choice = False
			elif inpt == '2' and skill == '3':
				os.system('clear')
				print '/----------------------------------------\ ', '\n',\
					  '|         My congratulations!            |', '\n',\
					  '|        Let`s evolve further.           |', '\n',\
					  '|    Maybe you`ll become Homosapiens.    |', '\n',\
					  '|                                        |', '\n',\
				      '|     As always you have few choices     |', '\n',\
				      '|     to evolve. To eat and multiply.    |', '\n',\
				      '|  If you want use it, just tap `enter`. |', '\n',\
					  '\----------------------------------------/'
				ran_n = random.randint(25, 39)
				raw_input()
				skill = killing(ran_n, 20)
				os.system('clear')
				print '/----------------------------------------\ ', '\n',\
				      '| Great it`s already passed 1500 mln.yrs.|', '\n',\
					  '|    You ate enough, and now you are     |', '\n',\
					  '|  so powerfull that you can evolve to   |', '\n',\
					  '|       `Moss`, `Bracken Fenr` or        |', '\n',\
					  '|              `Seed Plants`             |', '\n',\
					  '|                                        |', '\n',\
					  '|           Make your choice:            |', '\n',\
					  '|     Press 1 to choose `Moss`           |', '\n',\
					  '|     Press 2 to choose `Bracken Fen`    |', '\n',\
					  '|     Press 1 to choose `Seed Plants`    |', '\n',\
					  '|                                        |', '\n',\
					  '|   And rememder everything depend on    |', '\n',\
					  '|              Your Choice!              |', '\n',\
				      '\----------------------------------------/'
			





			else:
				os.system('clear')
				print '/----------------------------------------\ ', '\n',\
			    	  '| Great.You can eat and multiply so mach |', '\n',\
					  '|  as you want. And you`ll be seen with  |', '\n',\
					  '|  the humans, when they discovered you  |', '\n',\
					  '|           after 1000 ml.yrs.           |', '\n',\
					  '|                                        |', '\n',\
					  '|                 BYE                    |', '\n',\
					  '|                                        |', '\n',\
			    	  '\----------------------------------------/'
				choice = False

		elif inpt == '2' or inpt == '1':
			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
		    	  '| Great.You can eat and multiply so mach |', '\n',\
				  '|  as you want. And you`ll be seen with  |', '\n',\
				  '|  the humans, when they discovered you  |', '\n',\
				  '|           after 1000 ml.yrs.           |', '\n',\
				  '|                                        |', '\n',\
				  '|                 BYE                    |', '\n',\
				  '|                                        |', '\n',\
		    	  '\----------------------------------------/'
			choice = False
		elif inpt == '3' and skill == '2':

			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
				  '|         My congratulations!            |', '\n',\
				  '|        Let`s evolve further.           |', '\n',\
				  '|    Maybe you`ll become Homosapiens.    |', '\n',\
				  '|                                        |', '\n',\
			      '|     As always you have few choices     |', '\n',\
			      '|     to evolve. To eat and multiply.    |', '\n',\
			      '|  If you want use it, just tap `enter`. |', '\n',\
				  '\----------------------------------------/'
			ran_n = random.randint(25, 39)
			raw_input()
			skill = killing(ran_n, 20)
			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
			      '| Great it`s already passed 2500 mln.yrs.|', '\n',\
				  '|    You ate enough, and now you are     |', '\n',\
				  '|  so powerfull that you can evolve to   |', '\n',\
				  '|        `Animals`or `Fly Agaric`        |', '\n',\
				  '|                                        |', '\n',\
				  '|           Make your choice:            |', '\n',\
				  '|     Press 1 to choose `Animals`        |', '\n',\
				  '|     Press 2 to choose `Fly Agaric`     |', '\n',\
				  '|                                        |', '\n',\
				  '|   And rememder everything depend on    |', '\n',\
				  '|              Your Choice!              |', '\n',\
			      '\----------------------------------------/'
			inpt = raw_input('>')



	













	elif inpt == '3':
		os.system('clear')
		print '/----------------------------------------\ ', '\n',\
			  '|         My congratulations!            |', '\n',\
			  '|            `Eubacteria`                |', '\n',\
			  '|        Let`s evolve further.           |', '\n',\
			  '|    Maybe you`ll become Homosapiens.    |', '\n',\
			  '|                                        |', '\n',\
		      '|     As always you have few choices     |', '\n',\
		      '|     to evolve. To eat and multiply.    |', '\n',\
		      '|  If you want use it, just tap `enter`. |', '\n',\
			  '\----------------------------------------/'
		ran_n = random.randint(25, 39)
		raw_input()
		skill = killing(ran_n, 20)
		os.system('clear')
		print '/----------------------------------------\ ', '\n',\
		      '| Great it`s already passed 3000 mln.yrs.|', '\n',\
			  '|    You ate enough, and now you are     |', '\n',\
			  '|  so powerfull that you can evolve to   |', '\n',\
			  '| `Arhaea`, `Eukariotes` or `Eubacteria`.|', '\n',\
			  '|                                        |', '\n',\
			  '|           Make your choice:            |', '\n',\
			  '|     Press 1 to choose `Spirochaetes`   |', '\n',\
			  '|     Press 2 to choose `E.coli`         |', '\n',\
			  '|                                        |', '\n',\
			  '|   And rememder everything depend on    |', '\n',\
			  '|              Your Choice!              |', '\n',\
		      '\----------------------------------------/'
		inpt = raw_input('>')
		if inpt == '1' and skill == '2':
			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
		    	  '| Great.You can eat and multiply so mach |', '\n',\
				  '|  as you want. And you`ll be seen with  |', '\n',\
				  '|  the humans, when they discovered you  |', '\n',\
				  '|           after 1500 mln.yrs.          |', '\n',\
				  '|                                        |', '\n',\
				  '|                 BYE                    |', '\n',\
				  '|                                        |', '\n',\
		    	  '\----------------------------------------/'
			choice = False
		else:
			os.system('clear')
			print '/----------------------------------------\ ', '\n',\
				  '|     Sorry!But you can evolve only to   |', '\n',\
				  '| E.coli, cause you haven`t enough skills|', '\n',\
		    	  '|    You can eat and multiply so mach    |', '\n',\
				  '|  as you want. And you`ll be seen with  |', '\n',\
				  '|  the humans, when they discovered you  |', '\n',\
				  '|           after 1500 mln.yrs.          |', '\n',\
				  '|                                        |', '\n',\
				  '|                 BYE                    |', '\n',\
				  '|                                        |', '\n',\
		    	  '\----------------------------------------/'
			choice = False

			#	choice = False