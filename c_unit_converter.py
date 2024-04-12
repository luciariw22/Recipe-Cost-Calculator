def kg_to_grams(kg):
    grams = kg * 1000
    return grams


def main():
    try:
        kg = float(input("Enter weight in kilograms: "))
        grams = kg_to_grams(kg)
        print(f"{kg} kilograms ({grams} grams.)")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
