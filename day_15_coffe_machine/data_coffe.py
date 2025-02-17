#This is the data coffe file
#This file contains the data of the coffe machine
#This file is used by the main file to get the data of the coffe machine

class coffe_machine:
    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.money = 0
        self.cost = 0
        self.user_choice = ""
    
    def make_coffe(self, user_choice):
        self.user_choice = user_choice
        self.cost = menu[user_choice]["cost"]
        if self.water < menu[user_choice]["water"]:
            return "Sorry there is not enough water."
        elif self.milk < menu[user_choice]["milk"]:
            return "Sorry there is not enough milk."
        elif self.coffee < menu[user_choice]["coffee"]:
            return "Sorry there is not enough coffee."
        else:
            self.water -= menu[user_choice]["water"]
            self.milk -= menu[user_choice]["milk"]
            self.coffee -= menu[user_choice]["coffee"]
            return self.process_coins()
    
    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * coins["quarters"]) + (dimes * coins["dimes"]) + (nickles * coins["nickles"]) + (pennies * coins["pennies"])
        if total < self.cost:
            return "Sorry that's not enough money. Money refunded."
        else:
            self.money += self.cost
            change = total - self.cost
            return f"Here is ${change} in change. Here is your {self.user_choice} ☕️. Enjoy!"
        
    def __str__(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}\n"
    
menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}
