#coding: utf-8
from time import sleep
from os import system
import sys
import re
import random
#####################################################################

def nn ():
    print('\n')

###################################







def Função1(pergunta, decisão, pergunta2, opinião, opinião2):
    aaa = 1
    bbb = 2
    while aaa < bbb:
        pgt1 = input(pergunta) #pgt1 (pergunta 1)

        if re.search(f'{decisão}', pgt1, re.IGNORECASE):
            bbb -= 1
            pgt2 = input(pergunta2)
            esc1 = random.choice([opinião, opinião2])
            sleep(1)
            print(esc1)
            sleep(1)
            system('cls')

        else:
            print('Não entendi :(')
            sleep(2)
            system('cls')
########################################################################################################################
########################################################################################################################
def Passeio():
    Função1('Ok, você vai passear em algum lugar?\n ', 'sim', 'Onde vai passeiar?\n ', 'Eu acho que e melhor você ficar em casa hoje. Tchau, não quero mais conversar!', 'Eu acho que você deveria mesmo sair um pouco :) Tchau!\n ')

def Noticias():
    Função1('Vix estou desatualizado de noticias, você tem alguma?\n ', 'sim', 'Me conta mais!\n ', 'Eu não quero saber, tchau!\n ', 'hmm não sabia, tchau já conversei por tempo de mais.\n ')
