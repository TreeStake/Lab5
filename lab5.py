from enum import Enum, auto
import random
class Fruit:
    def __init__(self, name, size, colour, taste):
        """
        Assigns values to the new object
        :param name:
        :param size:
        :param colour:
        :param taste:
        """
        self.__name = name
        self.__size = size
        self.__colour = colour
        self.__taste = taste

    @property
    def name(self):
        """
        :return: The func returns private variable name
        """
        return self.__name

    @property
    def size(self):
        """
        :return: The func returns private variable size
        """
        return self.__size

    @property
    def colour(self):
        """
        :return: The func returns private variable colour
        """
        return self.__colour

    @property
    def taste(self):
        """
        :return: The func returns private variable taste
        """
        return self.__taste

class Taste(Enum):
    SWEET = auto()
    SOUR = auto()
    NEUTRAL = auto()

class Topping(Enum):
    CHOCOLADE = auto()
    SALT = auto()
    LEMON = auto()

class FruitSalad:
    def __init__(self):
        """
        Assigns values to the new object
        """
        self.__ingredients = []

    def add_fruit(self, fruit):
        """
        Add fruit into salad
        :param fruit:
        """
        self.__ingredients.append(fruit)

    def choose_topping(self):
        """
        Chooses the desired topping
        :return: choosen topping
        """
        sweat_count = sum(1 for fruit in self.__ingredients if fruit.taste == Taste.SWEET)
        sour_count = sum(1 for fruit in self.__ingredients if fruit.taste == Taste.SOUR)

        if sweat_count > sour_count:
            return Topping.CHOCOLADE
        elif sweat_count < sour_count:
            return Topping.LEMON
        else:
            return Topping.SALT

    def mix_ingredients(self):
        """
        Mixes the salad
        """
        random.shuffle(self.__ingredients)

    def __str__(self):
        """
        Representation of the object in text form
        """
        return ",".join(fruit.name for fruit in self.__ingredients)

def main():
    """
    Initialization of 3 objects
    :return: chose topping and mixed salad
    """
    banana = Fruit("Банан", "середній", "жовтий", Taste.SWEET)
    apple = Fruit("Яблуко", "середнє", "червоне", Taste.SWEET)
    lemon = Fruit("Лимон", "малий", "жовтий", Taste.SOUR)

    salad = FruitSalad()
    salad.add_fruit(apple)
    salad.add_fruit(lemon)
    salad.add_fruit(banana)

    topping = salad.choose_topping()
    print(f"{topping.name}")

    print(f"{salad}")
    salad.mix_ingredients()
    print(f"Салат змішаний:{salad}")

main()