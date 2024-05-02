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


def measurement(question):
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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# gets expenses, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    amount_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Amount": amount_list,
        "Price": price_list
    }

    # loop to get component, amount and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, amount and item
        item_name = not_blank("Item name: ",
                              "The component name can't be "
                              "blank.")
        if item_name.lower() == "xxx":
            break

        amount = measurement("Amount:")

        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)

        # add item, amount, and price to lists
        item_list.append(item_name)
        amount_list.append(amount)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Amount'] \
                             * expense_frame['Price']

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# *** Main Routine starts here ***

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank. ")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ***

print()
print(variable_frame)
print()
