"""Create a class hierarchy of animals with at least 5 animals that have additional methods each."""


class Animals:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def sleep(self):
        print("Any animal sleep!!")

    def move(self):
        print("All animal must move to live ")

    def breath(self):
        print("Nothing can not live without oxygen")


class Falcon(Animals):

    def fly(self):
        print(f"The {self.name} flying  like real planes")

    def eat_meat(self):
        print(f"{self.name} eat meat")


class Shark(Animals):

    def swim_under_water(self):
        print(f"{self.type} can swim under water and that is fine")

    def breath_under_water(self):
        print(f"All {self.type} breath under water and can not living without it ")


class Bee(Falcon):

    def make_honey(self):
        print(f'The {self.name} make honey')

    def build_tunnels(self):
        print(f"Almost all {self.type} build develop living place")


class Alligator(Shark):

    def kill(self):
        print(f"Alligator is named {self.name} like kill other animals")


class Termites(Bee):

    def destroy(self):
        print("Termites destroyed a lot of house built with wood ")
