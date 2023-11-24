import random 

word_list = ["apple", "lemon", "avocado", "pear", "pineapple"] #A list of words to choose from


print(word_list)

word = random.choice(word_list)

print(word)

secret_word = list(word)

print(secret_word)

def ask_for_input() :

    guess = input("Guess a letter:")

    while len(guess) != 1 or guess.isalpha() == False:

        print("Invalid letter. Please, enter a single alphabetical character.")

        guess = input("Guess a letter:")

        if guess.isalpha() == True and len(guess) == 1:

            break

    check_guess(guess)

def check_guess(guess) :

    guess = guess.lower()

    if guess in secret_word :

        print(f"Good guess! {guess} is in the word.")

    else :

        print(f"Sorry, {guess} is not in the word. Try again.")

    return guess

ask_for_input()