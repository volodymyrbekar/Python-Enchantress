"""Create two classes: Laptop, Guitare, one for composition, another one for aggregation."""


class Laptop:
    def __init__(self, ):
        powerful_laptop = Apple("Power laptop from Apple is -  MacBook Pro ")
        thin_laptop = Apple("Thin and enough powerful laptop is - MacBook Air")
        self.laptops = [powerful_laptop, thin_laptop]

    def choose_laptop(self):
        print(self.laptops)
        for laptop in self.laptops:
            print(laptop.model)


class Apple:

    def __init__(self, model):
        self.model = model


comp = Laptop()
comp.choose_laptop()
