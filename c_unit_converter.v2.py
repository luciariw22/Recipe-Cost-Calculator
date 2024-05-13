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
            return None, None
        if response.endswith('kg'):
            original_amount = response
            converted_amount = float(response[:-2]) * 1000
            print("Amount:", original_amount)
            print("Converted amount:", original_amount, "g")
            return original_amount, converted_amount
        elif response.endswith('g'):
            if response[:-1].isdigit():
                print("Amount:", response)
                return response, float(response[:-1])
            else:
                print(error)
                continue
        elif response.endswith('ml'):
            print("Amount:", response)
            return float(response[:-2]), None
        else:
            try:
                amount = float(response)
                if amount <= 0:
                    print("Please enter a valid amount")
                    continue
                else:
                    valid = True
            except ValueError:
                print(error)
                continue
            print("Amount:", amount, response)
            return amount, None


# Main routine goes here

while True:
    original_amount, converted_amount = measurement("\nAmount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
                                                    "enter number with no unit): ")
    if original_amount is None:
        break
    print("Original ingredient amount:", original_amount)
    if converted_amount is not None:
        print("Converted amount:", converted_amount)
