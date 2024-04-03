# Functions go here

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


# ingredient name for testing
ingredient_name = ['eggs']


# gets measurements for ingredient
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


# Main routine goes here


# Call the measurement function
ingredient_amount = measurement()
print("Amount entered:", ingredient_amount)
