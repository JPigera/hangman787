import random 

word_list = ["apple", "lemon", "avocado", "pear", "pineapple"] #a list of words to choose from


print(word_list)

word = random.choice(word_list) # generates random word from the list

print(word)

secret_word = list(word) # splits the word up into a list of letters

print(secret_word)

def ask_for_input() : # function that asks the user for the input and makes sure it is a valid input

    guess = input("Guess a letter:")

    while len(guess) != 1 or guess.isalpha() == False:

        print("Invalid letter. Please, enter a single alphabetical character.")

        guess = input("Guess a letter:")
        
        if guess.isalpha() == True and len(guess) == 1:

            break

    check_guess(guess) # check guess function is called as part of the ask_for_input() function

def check_guess(guess) : # The function turns the input into lower case and then checks if the guess is in the secret word

    guess = guess.lower()

    if guess in secret_word :

        print(f"Good guess! {guess} is in the word.")

    else :

        print(f"Sorry, {guess} is not in the word. Try again.")

    return guess

ask_for_input()