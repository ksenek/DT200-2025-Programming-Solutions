##
#class scores 2

#lists for class scores
class_a_scores = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b_scores = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

#Maximum score for class A
class_a_max = class_a_scores[0]
for score in class_a_scores:
    if score > class_a_max:
        class_a_max = score

#Minimum score for class A
class_a_min = class_a_scores[0]
for score in class_a_scores:
    if score < class_a_min:
        class_a_min = score

#Mean score for class A
class_a_sum = 0
for score in class_a_scores:
    class_a_sum += score
class_a_mean = class_a_sum / len(class_a_scores)

#Maximum score for class B
class_b_max = class_b_scores[0]
for score in class_b_scores:
    if score > class_b_max:
        class_b_max = score

#Minimum score for class B
class_b_min = class_b_scores[0]
for score in class_b_scores:
    if score < class_b_min:
        class_b_min = score

#Mean score for class B
class_b_sum = 0
for score in class_b_scores:
    class_b_sum += score
class_b_mean = class_b_sum / len(class_b_scores)

#Maximum score for both classes
all_scores = class_a_scores + class_b_scores
all_max = all_scores[0]
for score in all_scores:
    if score > all_max:
        all_max = score

#Minimum score for both classes
all_min = all_scores[0]
for score in all_scores:
    if score < all_min:
        all_min = score

#Mean score for both classes
all_sum = 0
for score in all_scores:
    all_sum += score
all_mean = all_sum / len(all_scores)

#Print results
print("Class A:")
print("  Maximum score:", class_a_max)
print("  Minimum score:", class_a_min)
print("  Mean score:", class_a_mean)
print("Class B:")
print("  Maximum score:", class_b_max)
print("  Minimum score:", class_b_min)
print("  Mean score:", class_b_mean)
print("Both classes:")
print("  Maximum score:", all_max)
print("  Minimum score:", all_min)
print("  Mean score:", all_mean)
