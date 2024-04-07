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


def measurement():
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        response = input("Amount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
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


# Main routine goes here

ingredient_amount = measurement()
print("Ingredient amount:", ingredient_amount)

