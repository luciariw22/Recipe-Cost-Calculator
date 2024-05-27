import pandas


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


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


def measurement(question, error):
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        response = input(question).lower()
        if response == "xxx":
            return None

        if response.endswith('kg'):
            print("Amount:", response)
            unit_type = "kg"

        elif response.endswith('g'):
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
            print("Amount:", response)

            return amount, None

        return amount, unit_type


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# the data frame and subtotal
def get_ingredient_costs():
    # Set up dictionaries and lists
    ingredient_list = []
    store_amount_list = []
    amount_list = []
    price_list = []

    variable_dict = {
        "Ingredient": ingredient_list,
        "Store Amount": store_amount_list,
        "Recipe Amount": amount_list,
        "Price": price_list
    }

    # loop to get ingredient, amount, and price
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":

        print()
        # get name, store amount, amount, and price
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be "
                                    "blank.")
        if ingredient_name.lower() == "xxx":
            break

        store_amount, store_unit = measurement("Amount ingredient is bought in from store?: ",
                                               "Please enter a valid measurement")
        store_amount_list.append(store_amount)
        if store_unit == "kg":
            store_converted_amount = store_amount * 1000
        elif store_unit == "ml":
            store_converted_amount = store_amount
        else:
            store_converted_amount = store_amount

        print("Converted store amount:", store_converted_amount, "g" if store_unit is not None else "")

        amount, unit = measurement("Recipe Amount: ", "Please enter a valid measurement")
        amount_list.append(amount)

        if unit == "kg":
            converted_amount = amount * 1000
        elif unit == "ml":
            converted_amount = amount
        else:
            converted_amount = amount

        print("Converted recipe amount:", converted_amount, "g" if unit is not None else "")

        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)
        price_list.append(price)

        # add item to lists
        ingredient_list.append(ingredient_name)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Ingredient')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Price'] / store_converted_amount * converted_amount
    total_cost = expense_frame['Cost'].sum()
    expense_frame['Total Cost'] = total_cost
    expense_frame['Cost per serving'] = total_cost / serving_size

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency formatting
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# *** Main Routine starts here ***

# Get product name
recipe_name = not_blank("Recipe name: ", "The Recipe name can't be blank.")
serving_size = num_check("Serving size: ", "The serving size can't be blank and must be an integer. ", int)

variable_expenses = get_ingredient_costs()
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ***

print()
recipe_heading = "***** -- {} Recipe -- serves {} -- *****".format(recipe_name, serving_size)
print(recipe_heading)
print()
print(variable_frame.drop(columns=['Cost per serving', 'Total Cost']))  # Remove 'Cost per serving' columns from
# the variable_frame
print()

cost_per_serv_heading = "**** Total Costs ****"
print(cost_per_serv_heading)
print()
print("Total cost: ${:.2f}".format(variable_sub))
print()
print("Costs ${:.2f} per serving".format(variable_sub))






