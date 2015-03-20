# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:27:47 2015
@author: Rodrigo 
"""
import time
from random import randint
nomes = ["Lagarto", "Pedra", "Papel", "Tesoura", "Spoke"]
lista = ["13","15","24","21","32","35","41","43","54","52"] #Lista com combinações possíveis para o user ganhar.
draw = ["11","22","33","44","55"] # Lista com as combinações que empatam.
countpc = 0 #Contador de pontos do pc.
countuser =0 #Contador de pontos do user
i = 0
while i == 0:
    print(""" Escolha um:
            Lagarto = 1   Pedra = 2   Papel =3   Tesoura =4  Spoke =5""")
    pc = randint(1,5)
    user = input("Coloque o número de sua escolha:")
    print("Sua escolha:",nomes[int(user)-1]) #Imprime a escolha do user
    print("Escolha do pc:",nomes[pc-1]) #Imprime a escolha do pc
    x = user+str(pc) # x junta o valor de user com o valor de pc Ex: user=1 e pc=1  user+pc=11. Por isso tive de converter o valor de pc em uma string
    time.sleep(1)
    if lista.__contains__(x):
        print("Você ganhou 1 ponto!")
        countuser+=1
    elif draw.__contains__(x):
        print("Você empatou!")
        countuser*0
        countpc*0
    else:
        print("Você perdeu 1 ponto!")
        countpc+=1
    if countuser == 3:
        print("Parabéns! Você ganhou o jogo!")
        i = int(input("Para continuar jogando pressione 0: \n"))
        countpc*0
        countuser*0
    if countpc == 3:
        print("O PC ganhou o jogo!")
        i = int(input("Para continuar jogando pressione 0: \n"))
        countpc*0
        countuser*0
   
    
        
        
    



