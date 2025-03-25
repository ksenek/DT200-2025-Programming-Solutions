##conversion program from menu
#program must take parameters and use returns


#functions for each conversion method with parameters and return statements
def knots_to_kmph(knots):
    """Converts knots to kmph.
    Returns the converted number.
    """
    return knots * 1.852

def feet_to_cm(feet):
    """Converts feet to cm.
    Returns the converted number.
    """
    return feet * 30.48

def inches_to_cm(inches):
    """Converts inches to cm.
    Returns the converted number.
    """
    return inches * 2.54

def cups_to_grams(cups):
    """Converts cups to grams.
    Returns the converted number.
    """
    return cups * 236.588

def menu():
    """Lists the different conversion modes.
    Checks the input is valid.
    Returns the chosen mode.
    """
    while True:
        try:
            choice = int(input("Welcome to my conversion program. \n1. Knots to km/h\n2. Feet to cm\n3. Inches to cm\n4. Cups to grams\n0. Quit\nEnter option: "))
            if choice in [0, 1, 2, 3, 4]:
                return choice
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

   
#main routine
if __name__ == "__main__":
    again = True
    while again:
        choice = menu()
        #gets unit input, and inputs unit parameter
        #gets input converted, uses the unit input as a parameter
        #goes to print function with right parameters
        
        if choice == 0:
            again = False
        elif choice == 1:
            knots = float(input("Enter knots: "))
            kmph = knots_to_kmph(knots)
            print("{:.2f} knots is equivalent to {:.2f} km/h.".format(knots, kmph))
        elif choice == 2:
            feet = float(input("Enter feet: "))
            cm = feet_to_cm(feet)
            print("{:.2f} feet is equivalent to {:.2f} cm.".format(feet, cm))
        elif choice == 3:
            inches = float(input("Enter inches: "))
            cm = inches_to_cm(inches)
            print("{:.2f} inches is equivalent to {:.2f} cm.".format(inches, cm))
        elif choice == 4:
            cups = float(input("Enter cups: "))
            grams = cups_to_grams(cups)
            print("{:.2f} cups is equivalent to {:.2f} grams.".format(cups, grams))
        else:
            print("Invalid input. Please try again.")


    
