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


# geta measurements for ingredient
def measurement():
    # Initialize variables and error message
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        # Ask for the amount needed for the recipe
        response = input("Amount needed for recipe? (e.g., 500g or 5) ")

        # Check if the measurement is in grams
        if response[-1] == "g":
            measurement_type = "g"
            amount = response[:-1]
        else:
            measurement_type = "unknown"
            amount = response

        try:
            # Check if the amount is more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue

        if measurement_type == "unknown" and amount > 10:
            grams_type = yes_no("Do you mean {:.0f}g, i.e., {:.0f} grams? "
                                "y / n ".format(amount, amount))
            # Set measurement type based on user answer
            if grams_type == "yes":
                measurement_type = "g"
            else:
                measurement_type = ""
        elif measurement_type == "unknown" and amount < 10:
            ingredient_type = yes_no("Do you mean {:.0f}, {}? "
                                     "y / n".format(amount, ingredient_name[0]))
            if ingredient_type == "yes":
                measurement_type = ""
        # Return the amount for the recipe
        if measurement_type == "g":
            return amount


# ====== Main routine goes here ======

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

product_name = not_blank("Recipe name: ", "The product name can't be blank. ")

while True:
    ingredient_name = not_blank("Ingredient: ", "The ingredient name can't be blank. ")
    ingredient_amount = measurement()
    print("Amount entered:", ingredient_amount)

    if ingredient_name == "xxx":
        break

# Call the measurement function
ingredient_amount = measurement()
print("Amount entered:", ingredient_amount)
