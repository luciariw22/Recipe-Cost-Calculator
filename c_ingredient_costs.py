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
    while True:
        response = input(question)
        if response.strip() == "":
            print("{}. \nPlease try again.\n".format(error))
        else:
            return response


def measurement(question, error):
    error = "Please enter a valid measurement\n"
    while True:
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
                return amount, unit_type

        except ValueError:
            print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# the data frame and subtotal
def get_ingredient_costs():
    ingredient_list = []
    store_amount_list = []
    amount_list = []
    price_list = []
    cost_list = []

    variable_dict = {
        "Ingredient": ingredient_list,
        "Store Amount": store_amount_list,
        "Recipe Amount": amount_list,
        "Price": price_list,
        "Cost": cost_list
    }

    ingredient_name = ""
    while ingredient_name.lower() != "xxx":
        print()
        ingredient_name = not_blank("Ingredient name: ",
                                    "The ingredient name can't be "
                                    "blank.")

        if ingredient_name.lower() == "xxx":
            if not ingredient_list:
                print("\nNo ingredients for recipe entered. Exiting program... ")
                return None, None  # Return None values to indicate no ingredients entered

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

        price = num_check("Price of ingredient? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)
        price_list.append(price)

        cost = price / store_converted_amount * converted_amount
        cost_list.append(cost)

        ingredient_list.append(ingredient_name)

    if not ingredient_list:
        print("\nNo ingredients for recipe entered. Exiting program... ")
        return None, None  # Return None values to indicate no ingredients entered

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Ingredient')

    sub_total = expense_frame['Cost'].sum()

    expense_frame['Total Cost'] = sub_total

    return expense_frame, sub_total


# *** Main Routine starts here ***

recipe_name = not_blank("Recipe name: ", "The Recipe name can't be blank.")
serving_size = num_check("Serving size: ", "The serving size can't be blank and must be a whole integer higher than 0. ", int)

variable_expenses, variable_sub = get_ingredient_costs()

if variable_expenses is not None:
    variable_frame = variable_expenses

    print()
    recipe_heading = "***** -- {} Recipe -- serves {} -- *****".format(recipe_name, serving_size)
    print(recipe_heading)
    print()
    print(variable_frame.drop(columns=['Cost per serving', 'Total Cost']))  # Remove Cost per serving columns from main frame
    print()

    cost_per_serv_heading = "**** Cost per Serving ****"
    print(cost_per_serv_heading)
    print()
    print("Total cost: ${:.2f}".format(variable_sub))
    print()
    print("Cost per serving: ${:.2f}".format(variable_sub / serving_size))
    print()

