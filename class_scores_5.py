##
#class_scores_5.py

#List initial scores for both classes
class_a_scores = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b_scores = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

def calculate_scores(scores):
    """Function to calculate the minimum, maximum and mean scores for a given list of scores"""
    minimum_score = scores[0]
    maximum_score = scores[0]
    total_score = 0
    for score in scores:
        if score < minimum_score:
            minimum_score = score
        if score > maximum_score:
            maximum_score = score
        total_score += score
    mean_score = total_score / len(scores)
    return minimum_score, maximum_score, mean_score


def modify_score(class_choice, scores):
    """Function to modify a score in either of the two classes"""
    index = int(input(f"Enter the index of the score you want to modify in Class {class_choice}: "))
    if index < 0 or index >= len(scores):
        print("Index out of range. No modification done.")
        return
    new_score = int(input("Enter the new score: "))
    scores[index] = new_score



def menu():
    """Function to display menu and handle user choice"""
    print("Menu:")
    print("1. Add a score")
    print("2. Modify a score")
    print("3. Quit")

    choice = input("Enter your choice: ")
    return choice

#Main loop to allow the user to add or modify scores
if __name__ == '__main__':
    while True:
        choice = menu()

        if choice == "1":
            class_choice = input("Enter A or B to add a score to that class: ")
            if class_choice.upper() == "A":
                score = int(input("Enter the score to add to Class A: "))
                class_a_scores.append(score)
            elif class_choice.upper() == "B":
                score = int(input("Enter the score to add to Class B: "))
                class_b_scores.append(score)
            else:
                print("Invalid input, please try again.")
        elif choice == "2":
            class_choice = input("Enter A or B to modify a score in that class: ")
            if class_choice.upper() == "A":
                modify_score("A", class_a_scores)
            elif class_choice.upper() == "B":
                modify_score("B", class_b_scores)
            else:
                print("Invalid input, please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select again.")

    #Recalculate the minimum, maximum and mean scores for both classes and print them out again
    min_a, max_a, mean_a = calculate_scores(class_a_scores)
    min_b, max_b, mean_b = calculate_scores(class_b_scores)
    min_both, max_both, mean_both = calculate_scores(class_a_scores + class_b_scores)
    print("Updated Class A minimum score:", min_a)
    print("Updated Class A maximum score:", max_a)
    print("Updated Class A mean score:", mean_a)
    print("Updated Class B minimum score:", min_b)
    print("Updated Class B maximum score:", max_b)
    print("Updated Class B mean score:", mean_b)
    print("Updated both classes minimum score:", min_both)
    print("Updated both classes maximum score:", max_both)
    print("Updated both classes mean score:", mean_both)
