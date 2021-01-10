from abc import ABC, abstractmethod
import random


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

        self.houses = {40: 500, 50: 600, 60: 700}

    def information_about_all_houses(self):
        [print(f"We are selling such houses - area:{areas} cost: {costs}") for areas, costs in self.houses.items()]

    def give_discount(self):
        for house in self.houses:
            if house <= 40:
                self.discount = 200

    @staticmethod
    def steal_money():
        money_heist = random.randint(0, 9)
        if money_heist == 1:
            print(f"Money is heist, {money_heist} ")
        else:
            print(f"Mission Fail ")


class Person(ABC):
    def __init__(self, name, age, money, own_home):
        self.name = name
        self.age = age
        self.money = money
        self.own_home = own_home

    @abstractmethod
    def provide_information_about_yourself(self):
        raise NotImplementedError("You miss me!")

    @abstractmethod
    def earn_money(self):
        raise NotImplementedError("You miss me!")

    @abstractmethod
    def buy_a_house(self):
        raise NotImplementedError("You miss me")


class House(ABC):

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        raise NotImplementedError("You miss me!")


class Human(Person):
    def __init__(self, name, age, money, own_home):
        super(Human, self).__init__(name, age, money, own_home)

    def provide_information_about_yourself(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and I wanna buy a house ")

    def earn_money(self):
        while self.money < 500:
            self.money += 100
        print(f"Now I have {self.money} y.e. and i will buy a house,")
        self.buy_a_house()

    def buy_a_house(self):
        if self.own_home is False and self.money >= 400:
            self.own_home = True
        print(f'I have a house - {self.own_home}')


class Home(House):

    def __init__(self, area, cost):
        super(Home, self).__init__(area, cost)
        self.cost = cost

    def apply_discount(self):
        if self.cost >= 500 and self.area <= 40:
            print("Discount is possible")
        print(f"This house with {self.area} square fit and cost - {self.cost}, don't have discount")


if __name__ == "__main__":
    realtor = Realtor(name="Nick", discount=200)
    realtor.give_discount()
    realtor.information_about_all_houses()
    realtor.steal_money()
    home = Home(area=50, cost=400)
    human = Human(name="John", age=22, money=0, own_home=False)
    home.apply_discount()
    human.earn_money()
