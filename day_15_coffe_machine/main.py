##this is the Coffe machine project
##this project is a coffe machine project

import data_coffe

def coffe_machine():
    user_choice = "on"
    machine = data_coffe.coffe_machine()  
    while user_choice != "off":
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "report":
            print(machine)  
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            print(machine.make_coffe(user_choice))
        elif user_choice == "off":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    coffe_machine()