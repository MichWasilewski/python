from utillies import calculations
from utillies import except_exception

def display():
    choice = None
    while choice != 'c':
        choice = input(
            """ 
            Proszę wybrać następujące opcję:
            c - koniec
            + - dodawanie
            - - odejmowanie
            * mnożenie
            / dzielenie
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