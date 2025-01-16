# Arbeidskrav 2

import numpy as np

# Oppgave 1
def oppgave_1():
    alder = int(input('Hvilket år er du født? '))
    alder_beregnet = 2024 - alder
    print('I løpet av år 2024, blir du: ' + str(alder_beregnet) + ' år gammel.')

# Oppgave 2
def oppgave_2():
    antall_elever = int(input('Skriv inn antall elever: '))
    antall_pizzaer = int(np.ceil(antall_elever/4))
    print('Det trengs å handle inn ' + str(antall_pizzaer) + ' pizzaer til festen.')

# Oppgave 3
def oppgave_3():
    v_grad = float(input('Skriv inn gradtallet: '))
    v_rad = v_grad * np.pi/180
    print('Gradtallet ' + str(v_grad) + ' gjort om til radianer er: ' + str(round(v_rad, 4)))

# Oppgave 4
def oppgave_4():

    # b

    data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.892],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873],
    }

    land = input('Hvilket land: ')
    hovedstad = data[land][0]
    innbyggere = str(data[land][1])

    print(hovedstad + ' er hovedstaden i ' + land + ' og det er ' + innbyggere + ' mill. innbyggere i ' + hovedstad)

    # c

    land = str(input('Hvilket nytt land vil du tilføye: '))
    hovedstad = str(input('Hva er hovedstaden i ' + land + ': '))
    innbyggere = float(input('Hvor mange innbyggere er det i ' + hovedstad + ': '))

    data[land] = [hovedstad, innbyggere]

    print(data)

# Oppgave 5
def oppgave_5():
    a = float(input('a: '))
    b = float(input('b: '))

    sirkel_areal = (np.pi * (a/2)**2) / 2
    sirkel_omkrets = np.pi * (a/2)

    trekant_areal = (a * b) / 2
    trekant_omkrets = b + (np.sqrt(a**2 + b**2))

    totalt_areal = round(sirkel_areal + trekant_areal, 4)
    totalt_omkrets = round(sirkel_omkrets + trekant_omkrets, 4)

    print('Arealet til figuren: ' + str(totalt_areal))
    print('Omkretsen til figuren: ', str(totalt_omkrets))

# Oppgave 6

import matplotlib.pyplot as plt

def oppgave_6():
    x = np.linspace(-10, 10, 200)

    def f(x):
        return -x**2 - 5
    
    plt.plot(x, f(x))

    plt.show()

oppgave_1()
oppgave_2()
oppgave_3()
oppgave_4()
oppgave_5()
oppgave_6()