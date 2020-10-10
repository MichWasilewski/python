def user_input(number_inputs):
    a = []
    for i in range(number_inputs + 1):

        number = ''
        while number == '':
            try:
                number = int(input("Liczba: "))
            except (ValueError, TypeError):
                print("Zła wartość")
            else:
                a.append(number)
    return a










# def user_input(division = False) -> str:
#     ui = input("Liczba: ")
#     if division and '0' == ui:
#         user_input()
#         raise ZeroDivisionError
#     try:
#         input_intiger = int(ui)
#
#     except ValueError as e:
#         print("Wpisz cyfrę !", e)
#         user_input()
#     #except Exception:
#         #print('Exception') # klauzula obsługiwająca jakikolwiek wyjątek
#     except ZeroDivisionError as a:
#         print("Wspisałeś zły typ input'u", a) #klauzula obsługowająca jakikolwiek wyjątek i która przechwytuje zawartość
#     return input_intiger
