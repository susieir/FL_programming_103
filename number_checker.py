# Number checker program

def enter_an_integer():

    number = input("Enter a number >")
    valid_integer = False

    while not valid_integer:
        try:
            number = int(number)
            valid_integer = True
        except:
            number = input("Invalid. Enter a number > ")

def enter_a_float():

    number = input("Enter a number >")
    valid_float = False

    while not valid_float:
        try:
            number = float(number)
            valid_float = True
        except:
            number = input("Invalid. Enter a number > ")

valid_number = enter_a_float()

print("Thank You")

