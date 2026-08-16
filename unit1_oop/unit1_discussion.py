"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy
import random


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    CRITICAL_HIT_MULTIPLIER = 2

    def __init__(self, name, hit_points=100, attack=25):
        self._name = name
        self._hit_points = hit_points
        self._attack = attack
        self._is_alive = True

    def get_name(self):
        return self._name

    def get_hit_points(self):
        return self._hit_points

    def get_attack(self):
        return self._attack

    def is_alive(self):
        return self._is_alive

    def deduct_hit_points(self, amount):
        if not self.is_alive():
            return False
        else:
            self._hit_points -= amount
            if self._hit_points <= 0:
                self._is_alive = False
            return True

    def __str__(self):
        return f"Name: {self.get_name()}, HP: {
            self.get_hit_points()}, Attack: {self.get_attack()}"

    def attack(self, target):
        damage = self.get_attack
        if random.randint(1, 20) > 15:
            damage *= ParentClass.CRITICAL_HIT_MULTIPLIER
            print("Critical hit!")
        if target.deduct_hit_points(damage):
            print(f"{damage} damage dealt to {target.get_name()}")
            print(target)
        else:
            print(f"{target.get_name()} is already dead")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    SHIELD_COST = 1
    MAGIC_ATTACK_COST = 3

    def __init__(self, name, hit_points=100, attack=25, magic_attack=50, mana=10):
        super().__init__(name, hit_points, attack)
        self._magic_attack = magic_attack
        self._mana = mana

    def get_magic_attack(self):
        return self._magic_attack

    def get_mana(self):
        return self._mana

    def deduct_hit_points(self, amount):
        if self.get_mana() > 0:
            amount -= random.randint(0, 25)
            self._mana -= ChildClass.SHIELD_COST
        return super().deduct_hit_points(amount)

    def magic_attack(self, target):
        starting_hp = target.get_hit_points()
        if self.get_mana() >= ChildClass.MAGIC_ATTACK_COST:
            if target.deduct_hit_points(self.get_magic_attack()):
                self._mana -= ChildClass.MAGIC_ATTACK_COST
                print(f"{starting_hp - target.get_hit_points()} damage dealt to {
                      target.get_name()}")
                print(target)
            else:
                print(f"{target.get_name()} is already dead")
        else:
            print("not enough mana")

    def __str__(self):
        return f"{super().__str__()}, Magic attack: {self.get_magic_attack()}, Mana: {self.get_mana()}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    player1 = ChildClass("Carl")
    player2 = ChildClass("Prepotente", attack=15, magic_attack=65, mana=25)

    print(f"It costs {ChildClass.MAGIC_ATTACK_COST} mana to cast a spell")
    print(f"{player1.get_name()} uses {
          player1.MAGIC_ATTACK_COST} mana to cast his spell")
    player1._inventory = ["Ring of Divine Suffering"]

    print(player1.__dict__)
    print(player2.__dict__)
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")
    object1 = ChildClass("Doughnut")
    object2 = object1
    object3 = deepcopy(object1)

    object1._name = "Mongo"
    object3.magic_attack(object1)

    print("Object 1: ", object1)
    print("Object 2: ", object2)
    print("Object 3: ", object3)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    player1 = ParentClass("Carl")
    player2 = ChildClass("Tina")

    print("\nTODO: Create and test your child object")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
