"""
Armando Cedano
M03 Custom Data Class 2
This code is the main class to run a couple unique instances of the coffee maker class and print it to the console
"""

# File: main.py

from coffee_maker import CoffeeMaker

def main():
    # Instantiate two unique instances of CoffeeMaker
    coffee_maker1 = CoffeeMaker("Keurig", "K-Elite", 48, "Black", True)
    coffee_maker2 = CoffeeMaker("Nespresso", "VertuoPlus", 60, "Red", False)

    # Print details of the coffee makers
    print(coffee_maker1)
    print(coffee_maker2)

if __name__ == "__main__":
    main()
