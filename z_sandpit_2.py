while True:
    ingredient_name = not_blank("\nIngredient: (or enter 'xxx' to when done) ", "The ingredient name can't be blank ")
    if ingredient_name == "xxx":
        break
    packaged_amount = measurement("\nAmount ingredient is bought in?: (e.g., 2kg, 200g, 20mL, or "
                                  "enter number with no unit): ")

    print("Packaged amount:", packaged_amount)

    ingredient_amount = measurement("\nAmount of ingredient needed for recipe?: (e.g., 2kg, 200g, 20mL, or "
                                    "enter number with no unit): ")

    print("Ingredient amount:", ingredient_amount)


