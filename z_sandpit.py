# Functions go here


# checks input is a float or integer
def instructions():
    print()
    print("instructions go here...")
    print()


# number checker
def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# yes / no checker
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# Checks input isn't blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


# ====== Main routine goes here ======

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

product_name = not_blank("Recipe name: ", "The product name can't be blank. ")

while True:
    ingredient_name = not_blank("Ingredient: ", "The ingredient name can't be blank. ")
    amount = num_check("Amount of ingredient?: ", "Please enter an integer more than 0. ", int)
    response = input("Measurement? (e.g. g, kg, mL, or no unit for whole amount): ")

    if response in ["g", "kg", "mL"]:
        measurement_type = response

    elif response == "":
        measurement_type = "whole"

    else:
        print("Please enter a valid measurement")

    if response in ["g", "kg", "mL"] or "":
        print(ingredient_name, amount, response)
