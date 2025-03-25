##
#class scores 1

#Define the scores for Class A and Class B
class_a_scores = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b_scores = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

#Combine the scores into one list
all_scores = class_a_scores + class_b_scores

#Calculate the lowest score
lowest_score = all_scores[0]
for score in all_scores:
    if score < lowest_score:
        lowest_score = score

#Calculate the highest score
highest_score = all_scores[0]
for score in all_scores:
    if score > highest_score:
        highest_score = score

#Calculate the mean score
total_score = 0
for score in all_scores:
    total_score += score
mean_score = total_score / len(all_scores)

#Print the results
print("Lowest score:", lowest_score)
print("Highest score:", highest_score)
print("Mean score:", mean_score)
