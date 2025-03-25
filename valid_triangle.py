def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

##is_triangle(1, 2, 3) # it's possible to arrange a triangle
##is_triangle(1, 2, 9) # it's not possible to arrange a triangle
##print()



if __name__ == "__main__":

    a = float(input("Enter the length of the first straw: "))
    b = float(input("Enter the length of the second straw: "))
    c = float(input("Enter the length of the third straw: "))

    if is_triangle(a, b, c):
        print("These lengths can form a triangle.")
    else:
        print("These lengths cannot form a triangle.")
