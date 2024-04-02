#třída Human
class Human:
    def __init__(self, name, contact, city=None):
        self.__name = name
        self.contact = contact
        self.city = city

    def get_name(self):
        return self.__name #__name je soukromé nastavení uvnitř funkce nelze zvenku číst ani měnit

    def set_name(self, new_name):
        if len(new_name) < 3:
            return False
        self.__name = new_name
        return True

h1 = Human("Human1", contact="contact1")
h2 = Human("Human2", contact="contact2", city="city")

#použití třídy
print(h1.get_name())
#h1.__name == "Nové jméno" # nebude funguovat kvůli privátní fce __name
h1.set_name("Nové jméno")
print(h1.get_name())



