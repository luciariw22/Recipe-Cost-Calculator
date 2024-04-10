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


# gets ingredient amounts and measurements
def measurement():
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        response = input("\nAmount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
                         "enter number with no unit): ").strip().lower()

        if response.endswith('kg'):
            print("Amount:", response)
            unit_type = "kg"

        elif response.endswith('g'):
            # Check if the substring before 'g' is numeric
            if response[:-1].isdigit():
                print("Amount:", response)
                unit_type = "g"
            else:
                print(error)
                continue

        elif response.endswith('ml'):
            print("Amount:", response)
            unit_type = "ml"

        else:
            unit_type = response

        try:
            if unit_type == "g":
                amount = float(response[:-1])
            elif unit_type == "kg" or unit_type == "ml":
                amount = float(response[:-2])
            else:
                amount = float(response)

            if amount <= 0:
                print("Please enter a valid amount")
                continue
            else:
                valid = True
        except ValueError:
            print(error)
            continue

        if unit_type == response:
            # If no unit is entered, return the amount directly
            return amount

        if unit_type == "g" or unit_type == "kg" or unit_type == "ml":
            return amount


# ====== Main routine goes here ======

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

product_name = not_blank("Recipe name: ", "The product name can't be blank. ")
serving_size = not_blank, num_check("Serving Size: ", "The serving size can't be blank "
                                                      "and must be an integer", int)

while True:
    ingredient_name = not_blank("\nIngredient: (or enter 'xxx' to when done) ", "The ingredient name can't be blank ")
    if ingredient_name == "xxx":
        break
    ingredient_amount = measurement()
    print("Amount entered:", ingredient_amount)
