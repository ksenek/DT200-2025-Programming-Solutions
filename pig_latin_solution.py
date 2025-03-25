##
# pig_latin.py
# Takes in a sentence from the user and converts it to pig latin
# Author:
# Date:


def vowel_convert(word):
    """
    Accepts a word that starts with a vowel
    Appends way to the end of the word and returns it
    """
    return word + "way"


def consonant_convert(word):
    """
    Accepts a word that starts with a consonant
    Returns the word in pig latin
    """
    vowel_index = 0
    first = False
    # Find the index of the first vowel
    for char in word:
        if char in VOWELS and not first:
            vowel_index = word.index(char)
            first = True

    # Get the slice of the vowel rearrange
    new_word = word[vowel_index:] + word[:vowel_index] + "ay"

    # return the new word
    return new_word
            

def vowel_check(word):
    """
    Checks if a word starts with a vowel or a consonant
    Returns true if it starts with vowel
    """
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    if word[0] in VOWELS:
        return True
    else:
        return False


def input_sentence():
    """
    Accepts a sentence and breaks it up into words
    Returns a list of words
    """
    sentence = input("Enter in a sentence: ")
    words = sentence.split(" ")
    return words


# Main routine
if __name__ == "__main__":
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    pig_sentence = []
    words = input_sentence()
    for word in words:
        if vowel_check(word):
            pig_sentence.append(vowel_convert(word))
        else:
            pig_sentence.append(consonant_convert(word))
    
    print(" ".join(pig_sentence))
