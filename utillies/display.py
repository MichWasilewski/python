from utillies import calculations
import datetime
import json

def display():
    name = " "
    with open('data.txt') as json_file:
        data = json.load(json_file)
    while name == " ":
        name = input("Podaj imię: ")
        x = datetime.datetime.now()
        choice = None

        data["how many"] += 1

        with open('data.txt', 'w+') as outfile:
            json.dump(data, outfile)

        print(f"Witaj ! {name}", "Synchronizujmy nasze smartwatch'e....jest teraz ", x)
        print("Twoja ilość logowań to: ", data["how many"])

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
            try:
                first = int(input("1 Liczba: "))
                second = int(input("2 Liczba: "))
                equel = calculations.multiplication(first, second)
                print("Wynik: ", equel)
            except (ValueError, TypeError) as e:
                print("Wpisz liczbę całkowitą", e)

        elif choice == '+':
            try:
                first = int(input("1 Liczba: "))
                second = int(input("2 Liczba: "))
                equel = calculations.addiction(first, second)
                print("Wynik: ", equel)
            except (ValueError, TypeError) as e:
                print("Wpisz liczbę całkowitą", e)

        elif choice == '-':
            try:
                first = int(input("1 Liczba: "))
                second = int(input("2 Liczba: "))
                equel = calculations.subtraction(first, second)
                print("Wynik: ", equel)
            except (ValueError, TypeError) as e:
                print("Wpisz liczbę całkowitą", e)

        elif choice == '/':

            try:
                first = int(input("1 Liczba: "))
                second = int(input("2 Liczba: "))
                equel = calculations.division(first, second)
                print("Wynik: ", equel)
            except (ValueError, TypeError) as e:
                print("Wpisz liczbę całkowitą", e)
            except ZeroDivisionError as z:
                print("Nie dzielimy przez 0 !", z)



    print("\nDowidzenia !")