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
            converted_amount = float(response[:-2]) * 1000

        elif response.endswith('g'):
            if response[:-1].isdigit():
                print("Amount:", response)
                unit_type = "g"
                converted_amount = float(response[:-1])
            else:
                print(error)
                continue

        elif response.endswith('ml'):
            print("Amount:", response)
            unit_type = "ml"
            converted_amount = float(response[:-2])

        else:
            unit_type = response
            converted_amount = float(response)

        try:
            if converted_amount <= 0:
                print("Please enter a valid amount")
                continue
            else:
                valid = True
        except ValueError:
            print(error)
            continue

        return converted_amount


# Main routine goes here

while True:
    converted_amount = measurement("\nAmount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
                                   "enter number with no unit): ")
    if converted_amount is None:
        break
    print("Converted amount:", converted_amount, "g")  # No need to separately calculate converted_amount

