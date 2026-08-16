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
    """A dungeon crawler class

    Attributes:
        name: the name of the dungeon crawler
        hit_points: the amount of hit points (default 100)
        attack: the amount of normal attack damage (default 25)
        is_alive: the status of the crawler
    """
    CRITICAL_HIT_MULTIPLIER = 3

    def __init__(self, name, hit_points=100, attack=25):
        """Create a new dungeon crawler instance

        Args:
            name: the name of the dungeon crawler
            hit_points: the amount of hit points (default 100)
            attack: the amount of normal attack damage (default 25)
        """
        self._name = name
        self._hit_points = hit_points
        self._attack = attack
        self._is_alive = True

    def get_name(self):
        """returns the crawler's name"""
        return self._name

    def get_hit_points(self):
        """returns the crawler's remaining hit points"""
        return self._hit_points

    def get_attack(self):
        """returns the crawler's attack damage"""
        return self._attack

    def is_alive(self):
        """returns True if the crawler is still alive, False if dead"""
        return self._is_alive

    def deduct_hit_points(self, amount):
        """Deduct a specified amount of hit points from the crawler

            Prints a status update to STDOUT if the crawler dies and changes the 
            crawler's alive status.

        Args:
            amount: the amount of damage to be applied

        Returns: 
            True if the damage was deducted, False if otherwise
        """
        if not self.is_alive():
            return False
        else:
            self._hit_points -= amount
            if self._hit_points <= 0:
                print(f"{self.get_name()} has died", "\n")
                self._is_alive = False
            return True

    def __str__(self):
        """Overloaded __str__ method

        Print(crawler_object) will print the crawler's name, remaining hit points, and status

        Returns:
            a formatted string with the crawler's information
        """
        return f"Name: {self.get_name()}, HP: {
            self.get_hit_points()}, Attack: {self.get_attack()}, Alive?: {self.is_alive()}"

    def attack(self, target):
        """Basic Attack

        Displays the amount of damage dealt and the target's information after each 
        successful attack.

        Args:
            target: another instance of the crawler class

        Returns:
            True if the attack is successful, False otherwise.
        """
        if not self.is_alive():
            print(f"{self.get_name()} can't attack when dead", "\n")
            return False
        damage = self.get_attack()
        if random.randint(1, 20) > 15:
            damage *= ParentClass.CRITICAL_HIT_MULTIPLIER
            print("Critical hit!")
        if target.deduct_hit_points(damage):
            print(f"{damage} damage dealt to {target.get_name()}", "\n")
            print(target, "\n")
            return True
        else:
            print(f"{target.get_name()} is already dead", "\n")
            return False


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
    """A defensive mage class with a damage reduction ability, extends crawler.

    Attributes:
        name: the name of the dungeon crawler
        hit_points: the amount of hit points (default 100)
        attack: the amount of normal attack damage (default 25)
        is_alive: the status of the crawler
        magic_attack: the amount of magic attack damage (default 50)
        mana: the amount of mana points remaining (default 10)
    """
    SHIELD_COST = 1
    MAGIC_ATTACK_COST = 3

    def __init__(self, name, hit_points=100, attack=25, magic_attack=50, mana=10):
        """Create a new defensive mage crawler instance

        Args:
            name: the name of the dungeon crawler
            hit_points: the amount of hit points (default 100)
            attack: the amount of normal attack damage (default 25)
            magic_attack: the amount of magic attack damage (default 50)
            mana: the amount of mana points remaining (default 10)
        """
        super().__init__(name, hit_points, attack)
        self._magic_attack = magic_attack
        self._mana = mana

    def get_magic_attack(self):
        """returns the crawler's magic attack damage"""
        return self._magic_attack

    def get_mana(self):
        """returns the crawler's remaining mana"""
        return self._mana

    def deduct_hit_points(self, amount):
        """applies a damage reduction to oncoming damage for a mana cost
            
        Overloaded method from parent class.

        Args:
            amount: the amount of damage to be applied
        """
        if self.get_mana() > 0:
            dmg_redux = random.randint(0, 25)
            amount -= dmg_redux
            self._mana -= ChildClass.SHIELD_COST
        return super().deduct_hit_points(amount)

    def magic_attack(self, target):
        """The mage crawler's magic attack. 

        Can only be used if there is enough remaining mana points. When the attack 
        is successful, the mana cost is applied to the crawler's remaining mana.

        Args:
            target: another instance of the crawler class

        Returns:
            True if the attack is successful, False otherwise.
        """
        if not self.is_alive():
            print(f"{self.get_name()} can't attack when dead", "\n")
            return False
        starting_hp = target.get_hit_points()
        if self.get_mana() >= ChildClass.MAGIC_ATTACK_COST:
            if target.deduct_hit_points(amount=self.get_magic_attack()):
                self._mana -= ChildClass.MAGIC_ATTACK_COST
                print(f"{starting_hp - target.get_hit_points()} damage dealt to {
                      target.get_name()}", "\n")
                print(target, "\n")
                return True
            else:
                print(f"{target.get_name()} is already dead", "\n")
                return False
        else:
            print("not enough mana", "\n")
            return False

    def __str__(self):
        """Overloaded __str__ method, returns superclass's __str__ function with
        mage specific information appended.
        """
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

    print(f"It costs {ChildClass.MAGIC_ATTACK_COST} mana to cast a spell\n")
    print(f"{player1.get_name()} uses {
          player1.MAGIC_ATTACK_COST} mana to cast his spell\n")
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

    #Shallow copy, the instance namespace of object2 matches object1
    object2 = object1 

    #Deep copy. the instance namespace of object3 is separate from the other 2 instances
    object3 = deepcopy(object1) 

    object1._name = "Mongo"
    object3.magic_attack(object1)

    print("Object 1: ", object1, "\n")
    print("Object 2: ", object2, "\n")
    print("Object 3: ", object3, "\n")


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

    player1 = ParentClass("Carl")
    player2 = ChildClass("Tina")

    print(player1, "\n")
    print(player2, "\n")

    for i in range(1, 11):
        print(f"===== Round {i} ======")
        if not player1.is_alive():
            print(f"fight over, {player2.get_name()} wins")
            break
        elif not player2.is_alive():
            print(f"fight over, {player1.get_name()} wins")
            break
        else:
            player1.attack(player2)
            player2.magic_attack(player1)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
