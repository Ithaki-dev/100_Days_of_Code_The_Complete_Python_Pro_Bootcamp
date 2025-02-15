##this is the Coffe machine project
##this project is a coffe machine project

import data_coffe

machine_status = True
user_choice = input("What would you like? (espresso/latte/cappuccino): ")  


while user_choice != "off":
    if user_choice == "report":
        print(data_coffe.coffe_machine())  
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        print(data_coffe.coffe_machine().make_coffe(user_choice))
    