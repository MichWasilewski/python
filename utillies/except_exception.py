def user_input(division = False) -> str:
    ui = input("1 Liczba: ")
    if division and '0' == ui:
        user_input()
        raise ZeroDivisionError
    try:
        input_intiger = int(ui)

    except ValueError as e:
        print("Wpisz cyfrę !", e)
        user_input()

    #except Exception:
        #print('Exception') # klauzula obsługiwająca jakikolwiek wyjątek
    except Exception as e:
        print("Wspisałeś zły typ input'u", e) #klauzula obsługowająca jakikolwiek wyjątek i która przechwytuje zawartość
    finally:
        print("Dziękuję !")
    return input_intiger
user_input()