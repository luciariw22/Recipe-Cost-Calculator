# functions go here
# checks that user's name is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("This can't be blank. Please try again")
        else:
            return response


# main routine goes here
while True:
    name = not_blank("\nEnter recipe name: (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")
