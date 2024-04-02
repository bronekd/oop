# vypočítat plochu tvaru
# Nechápu logiku tříd jak ji vytvořit podívat se k učitelovi


class Shape:

    def __init__(self, name):
        self.name = name

    def Calculate_area(self):
        raise NotImplementedError("Metoda musí být v potomcích")



#pokracovat comitem geometrypagace