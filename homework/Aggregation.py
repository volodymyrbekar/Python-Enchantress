""""Create two classes: Laptop, Guitare, one for composition, another one for aggregation."""

class Guitare:

    def __init__(self, string_num):
        self.string_num = string_num
        print(f"Guitare contains {self.string_num} strings")
class String:
    def __init__(self, material):
        self.material = material

    def type_of_material(self):
        print(f"The Strings are made with {self.material}")


guitar_string = String("plastic")
guitar_string.type_of_material()
guitar = Guitare(string_num=5)
