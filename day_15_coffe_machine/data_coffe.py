#This is the data coffe file
#This file contains the data of the coffe machine
#This file is used by the main file to get the data of the coffe machine

class coffe_machine:
    def __init__(self):
        self.machine_status = True
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.money = 0
        self.cost = 0
        self.user_choice = ""
    
    def __str__(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}\n"
    