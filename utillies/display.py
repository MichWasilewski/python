from utillies import calculations
from utillies.except_exception import user_input
from datetime import datetime
import json

def display():
    name = " "
    with open("data.json") as json_file:
        data = json.load(json_file)
    while name == " ":
        name = input("Podaj imię: ")
        x = datetime.now()
        choice = None

        if name not in data:
            data.update({name: 1})
        else:
            data[name] += 1#Tu imię

        with open("data.json", "w+") as outfile:
            json.dump(data, outfile)

        print(f"Witaj ! {name}", "Synchronizujmy nasze smartwatch'e....jest teraz ", x)
        print("Twoja ilość logowań to: ", data[name])

    while choice != 'c':
        choice = input(
            """ 
            Proszę wybrać następujące opcję:
            c - koniec
            + - dodawanie
            - - odejmowanie
            * - mnożenie
            / - dzielenie
            """)

        if choice == '*':
            first = user_input(2)
            equel = calculations.multiplication(*first)
            print("Wynik: ", equel)

        elif choice == '+':
            first = user_input(2)
            equel = calculations.addiction(*first)
            print("Wynik: ", equel)

        elif choice == '-':
            first = user_input(2)
            equel = calculations.subtraction(*first)
            print("Wynik: ", equel)

        elif choice == '/':
            first = user_input(2)
            equel = calculations.division(*first)
            print("Wynik: ", equel)

    print("\nDowidzenia !")