
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


def get_whole_amount():
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        response = input("\nAmount of ingredient when bought from store?: (e.g., 2kg, 200g, 20mL, or "
                         "enter number with no unit): ").strip().lower()
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


# main routine goes here
ingredient_cost = get_whole_amount()
print("Amount of ingredient in packaging:", ingredient_cost)
