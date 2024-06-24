def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        if response in to_check:
            return response
        else:
            print("Please enter either yes or no...\n")


def measurement(question):
    error = "Please enter a valid measurement\n"
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "xxx":
            return None

        # Extracting numeric part and unit part separately
        numeric_part = response[:-2]
        unit_part = response[-2:]

        if unit_part in ['kg', 'g', 'ml']:
            if numeric_part.isdigit():
                print("Amount:", response)
                return float(numeric_part), unit_part
            else:
                print(error)
        else:
            print(error)


def converted_amount(amount, unit_type):
    if unit_type == "kg":
        return amount * 1000
    elif unit_type == "g":
        return amount
    elif unit_type == "ml":
        return amount 


# Main routine goes here

while True:
    measurement_result = measurement("\nAmount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
                                     "enter number with no unit): ")
    if measurement_result is None:
        break

    amount, unit_type = measurement_result
    converted = converted_amount(amount, unit_type)
    print("Converted amount:", converted)

