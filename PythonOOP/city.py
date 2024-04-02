class City:
    def __init__(self, name, region_name, country_name = None, number_of_citizen = None, zip_code = None, area_code = None):
        self.name = name
        self.region_name = region_name
        self.country_name = country_name
        self.number_of_citizen = number_of_citizen
        self.zip_code = zip_code
        self.area_code = area_code

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        if len(new_name) < 3:
            return False
        self.name = new_name
        return True

    def get_region(self):
        return self.region_name

c1 = City("Brno", "Morava", "Cesko")



print(c1.get_name())
print(c1.get_region())





