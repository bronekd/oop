#třídy se píší s velkým písmenem

# toto využívám v souboru car
class Vehicle:
    def __init__(self, name):
    #inicializace při vytváření konkrétní třídy
        self.name = name

    def start(self): #Metoda fce uvnitř nějaké třídy
        print(f"vrvrvrvr startuju vozidlo {self.name}")

    def stop(self):
        print(f"vrvrvr ticho {self.name}")

"""
# vzor prní trénink
v1 = Vehicle("Vehicle1") #list()
v2 = Vehicle("Vehicle2")
v3 = Vehicle("Vehicle3")


print(v1.name)
print(v2.name)
print(v3.name)
print(type(v1))
print()

v2.start()

print()
v3.stop()
"""
