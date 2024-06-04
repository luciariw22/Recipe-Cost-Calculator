import pandas


# prints instructions
def instructions():
    print()
    print("instructions go here...")
    print()


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


# ensures inputs can't be blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response


# gets unit of amounts
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


# gets costs and puts them into lists
def get_ingredient_costs():
    # Set up dictionaries and lists
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

    # loop to get ingredient, amount, and price
    ingredient_name = ""
    while ingredient_name.lower() != "xxx":

        print()
        # get name, store amount, amount, and price
        ingredient_name = not_blank("Ingredient name: (or enter 'xxx' when done)",
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

        price = num_check("Cost to buy ingredient?: $",
                          "The price must be a number <more "
                          "than 0>",
                          float)
        price_list.append(price)

        # Calculate cost for the current ingredient
        cost = price / store_converted_amount * converted_amount
        cost_list.append(cost)

        # add item to lists
        ingredient_list.append(ingredient_name)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Ingredient')

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Calculate cost per serving
    expense_frame['Total Cost'] = sub_total
    expense_frame['Cost per serving'] = sub_total / serving_size

    # Currency formatting
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# ======== Main Routine starts here ========

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

# Get product name
recipe_name = not_blank("\nRecipe name: ", "The Recipe name can't be blank.")
serving_size = num_check("Serving size: ",
                         "The serving size can't be blank and must be a whole integer higher than 0. ", int)

variable_expenses = get_ingredient_costs()
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ***

print()
recipe_heading = "***** -- {} Recipe -- serves {} -- *****".format(recipe_name, serving_size)
print(recipe_heading)
print()
print(
    variable_frame.drop(columns=['Cost per serving', 'Total Cost']))  # Remove Cost per serving columns from main frame
print()

cost_per_serv_heading = "**** Cost per Serving ****"
print(cost_per_serv_heading)
print()
print("Total cost: ${:.2f}".format(variable_sub))
print()
print("Cost per serving: ${:.2f}".format(variable_sub / serving_size))
print()
