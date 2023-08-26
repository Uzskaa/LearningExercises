# Title: Count vowels in python using function
# This program tests whether a passed letter is a vowel or not.


def isVowel(char):
    vowels = "aeiou"
    for n in vowels:
        if n == char:
            isit = "VOWEL"
            break
        else:
            isit = "CONSONANT"
    print("the character is a", isit)


userInput = input("input a character: ")  
isVowel(userInput)
