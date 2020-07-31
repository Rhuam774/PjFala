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


def Passeio():
    aaa = 1
    bbb = 2
    while aaa < bbb:
        pgt1 = input('Ok, você vai passear em algum lugar?\n')

        if re.search('\\bsim\\b', pgt1, re.IGNORECASE):
            bbb -= 1
            pgt2 = input('Onde vai passeiar?\n')
            esc1 = random.choice(['Eu acho que e melhor você ficar em casa hoje. Tchau, não quero mais conversar!', 'Eu acho que você deveria mesmo sair um pouco :) Tchau!'])
            sleep(1)
            nn()
            print(esc1)
            sleep(1)
            system('cls')

        else:
            print('Não entendi :(')
            sleep(2)
            system('cls')
########################################################################################################################

