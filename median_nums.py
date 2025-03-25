def find_median(x, y, z):
    """
    This function takes three numbers as input and returns the median value of those parameters.
    """
    if x <= y <= z or z <= y <= x:
        return y
    elif y <= x <= z or z <= x <= y:
        return x
    else:
        return z

# main program to get user input and display median
if __name__ == "__main__":
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the third number: "))
    median = find_median(x, y, z)
    print("The median value of the three numbers is: ", median)
