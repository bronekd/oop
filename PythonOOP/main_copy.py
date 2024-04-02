# záčátek OOP
#import os

# toto je původní vzor main souboru zde je to jinde aby se s tím pracovalo jinak

def write_to_file(file_name, data):
    with open(file_name, "w") as file_handler:
        file_handler.write(data)
def reade_from_file(file_name):
    data = None
    with open(file_name, "r") as file_handler:
        data = file_handler.read()
    return data

MY_FILE = "file.txt"


# dává pro spouštění hlavního souboru
if __name__ == '__main__':
    MY_FILE = "file.txt"


    user_input = input("Zadej zprávu: ")
    write_to_file(MY_FILE, user_input)
    print("Zápis se provedl")

    data = reade_from_file(MY_FILE)
    print(data)
