#coding: utf-8
from time import sleep
from os import system
import sys
from PacoteP2 import Passeio
import re
######################
def T ():
    sleep(1)
######################
######################
def nn ():
    print('\n')
######################


nome_ass = 'PjFala'  #Nome da assistente.
print(f'olá eu sua assistente mais sirvo apenas pra conversar :)')
sleep(2)

print(f'Meu nome e {nome_ass}')
T()

print('Sobre o que você quer falar?')
T()
nn()

print('*Passeio?')
T()


print('*noticias?')
T()

print('*apenas bater um papo?')
T()
nn()
pgt1 = input('diz ai: ')

if re.search('\\bpasseio\\b', pgt1, re.IGNORECASE):
    Passeio()

elif pgt1 == 'noticias':
    print('Não quero falar sobre isso! \nTchau!')

else:
    print('Infelismente eu não quero conversar, Tchau!')


