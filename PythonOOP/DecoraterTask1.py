#moje řešení
#datetime knihovna
#vytisknout čas a odekorovat znakem hvězdičkou
#**************
#21:20
#**************
from datetime import datetime
def TimeDecor():
    print( "*********************************")

def TimePrint():
    print(datetime.now())


decor1 = TimeDecor()
decor2 = TimePrint()
# mě nefunguje hvězdičky nakonci

print()



# řešení učitel správné:



def my_curent_time():
    print("22:20")

def stars(myFunction):
    def simpleWrapper():
        print("*********************")
        myFunction()
        print("*********************")

    return simpleWrapper


curent_time = stars(my_curent_time)
curent_time()

print()
print()

#task 3. přepsat funkci výše do sintaxe se zavináčem více použivanou sintaksi

def stars2(myFunction):
    def simpleWrapper():
        print("*********************")
        myFunction()
        print("*********************")

    return simpleWrapper

@stars2
def my_curent_time_deco():
    print("20:22")

my_curent_time_deco()









