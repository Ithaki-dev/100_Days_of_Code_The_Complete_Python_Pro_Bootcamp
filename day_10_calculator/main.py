#This program is calculator that can do addition, subtraction, multiplication, division, exponentiation, and modulo operations.
#This program takes two numbers as input and performs the operation on them.

import calc
import art
import os


def calculator():
    print(art.logo)
    simbol_dict = {"+": "addition", "-": "subtraction", "*": "multiplication", "/": "division", "**": "exponentiation", "%": "modulo"}
    result = 0
    continue_calc = "y"
    while continue_calc == "y":
        if result != 0:
            number1 = result
            simbol = input("Enter operation: \n + for addition \n - for subtraction \n * for multiplication \n / for division \n ** for exponentiation \n % for modulo \n")
            number2 = float(input("Enter second number: "))
        else:
            number1 = float(input("Enter first number: "))
            simbol = input("Enter operation: \n + for addition \n - for subtraction \n * for multiplication \n / for division \n ** for exponentiation \n % for modulo \n")
            number2 = float(input("Enter second number: "))

        if simbol in simbol_dict:
            if simbol == "+":
                result = calc.add(number1, number2)
            elif simbol == "-":
                result = calc.subtract(number1, number2)
            elif simbol == "*":
                result = calc.multiply(number1, number2)
            elif simbol == "/":
                result = calc.divide(number1, number2)
            elif simbol == "**":
                result = number1 ** number2
            elif simbol == "%":
                result = number1 % number2
            print(f"{number1} {simbol} {number2} = {result}")
            continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        else:
            print("Invalid operation")
            continue_calc = input("Type 'y' to continue calculating, or type 'n' to start a new calculation: ")
    else:
        calculator()
        os.system('cls')

if __name__ == "__main__":
    calculator()