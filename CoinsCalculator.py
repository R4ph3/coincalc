# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:05:15 2021

@author: David & Raphe
"""

def calculadora_monedas(monedas, objetivo):

    days = 0
    while monedas<=objetivo:
        days += 1
        if days == dia_monedas:
           monedas = monedas + cantidad_monedas
        monedas = monedas * cantidad + monedas
        print(f"We are on day {days} and you have {monedas}")
        #return\
        #print(f'Tarda estos dias:{days}')

monedas=float(input('How many coins do you have: '))
objetivo=float(input('How many coins do you need: '))
cantidad=float(input("How many coins does a single one produce per day: "))
dia_monedas=int(input("In which day do you want to put more coins? Press 0 for none:"))
cantidad_monedas=float(input("Tell me the amount,press 0 for none:"))




calculadora_monedas(monedas,objetivo)

