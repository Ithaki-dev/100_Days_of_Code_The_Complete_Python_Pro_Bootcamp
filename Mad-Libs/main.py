##This is basic prgram about Mad Libs

#Here we ask the user to give us verbs and adjectives 
verb1 = input("Give me a verb: ")
verb2 = input("Give me a verb: ")
verb3 = input("Give me a verb: ")
verb4 = input("Give me a verb: ")


adjective = input("Give me a adgetive: ")
adjective2 = input("Give me a adgetive: ")
adjective3 = input("Give me a adgetive: ")
adjective4 = input("Give me a adgetive: ")

#mad_lib save the hole text were we change the verbs and adjectives

mad_lib = f"The {adjective} boy {adjective3} quickly through the {adjective2} forest, feeling {verb1} and {adjective3} at the same \
    time. His {verb2} legs {verb3} swiftly as he {verb4} for a {adjective3} treasure. The {adjective4} trees"

#We show the user the result with the changes.

print(mad_lib)