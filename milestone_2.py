import random 

word_list = ["Apple", "Lemon", "Avocado", "Pear", "Pineapple"] #A list of words to choose from

print(word_list)

word = random.choice(word_list) #choosing a random word from the list and assigning it to the variable 'word'

print(word)

guess = input("Enter a single letter:") #asks the user for an input of one letter

print(guess)



if len(guess) == 1 and guess.isalpha() == True : #if statement checks that the input is one letter and the charachter is a letter from the alphabet

    print("Good guess!")

else :
    print("Oops! That is not a valid input")
