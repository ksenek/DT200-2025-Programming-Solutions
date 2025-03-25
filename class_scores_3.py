##
#class socres 3
#List initial scores for both classes
class_a_scores = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b_scores = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

#Function to calculate the minimum, maximum and mean scores for a given list of scores
def calculate_scores(scores):
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

#Calculate the minimum, maximum and mean scores for both classes and print them out
min_a, max_a, mean_a = calculate_scores(class_a_scores)
min_b, max_b, mean_b = calculate_scores(class_b_scores)
min_both, max_both, mean_both = calculate_scores(class_a_scores + class_b_scores)
print("Class A minimum score:", min_a)
print("Class A maximum score:", max_a)
print("Class A mean score:", mean_a)
print("Class B minimum score:", min_b)
print("Class B maximum score:", max_b)
print("Class B mean score:", mean_b)
print("Both classes minimum score:", min_both)
print("Both classes maximum score:", max_both)
print("Both classes mean score:", mean_both)

#Allow the user to add scores to either of the two classes
if __name__ == '__main__':
    while True:
        class_choice = input("Enter A or B to add a score to that class, or Q to quit: ")
        if class_choice.upper() == "Q":
            break
        elif class_choice.upper() == "A":
            score = int(input("Enter the score to add to Class A: "))
            class_a_scores.append(score)
        elif class_choice.upper() == "B":
            score = int(input("Enter the score to add to Class B: "))
            class_b_scores.append(score)
        else:
            print("Invalid input, please try again.")

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
