# Function to check if input is a positive integer
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


# Main routine
while True:
    serving_amount = num_check("Serving amount?: ",
                               "The serving size must be a whole integer higher than 0. \n",
                               int)
    print("Program Continues")
    print()






