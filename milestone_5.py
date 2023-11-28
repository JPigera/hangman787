import random 

word_list = ["apple", "lemon", "avocado", "pear", "pineapple"] #a list of words to choose from


print(word_list)

class Hangman :

    def __init__(self, word_list, num_lives= 5) :

        self.word = random.choice(word_list) #The word to be guessed, picked randomly from the word_list
        self.word_guessed = [letter.replace(letter, "_") for letter in word_list] # list - A list of the letters of the word
        self.num_letters = len(set(self.word)) # int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives # int - The number of lives the player has at the start of the game.
        self.word_list = word_list #list - A list of words
        self.list_of_guesses = [] #list - A list of the guesses that have already been tried
        self.guess = input("Guess a letter:")

    def check_guess(self, guess) :
        '''This method takes in the users one character guess as a parameter.

        It makes the letter lower case then tells the user if it was a correct guess or an incorrect guess.

        If correct it will take the guess and replace "_" with the letter that has been guessed.

        If incorrect a message will read that the letter was not in the word and that the user numbers of lives has reduced by one
        
        '''

        self.guess = self.guess.lower()

        if self.guess in self.word :

            print(f"Good guess! {self.guess} is in the word.")

            index = -1

            for self.letter in self.word_list :
            
                index+=1

                if guess == self.letter :
                    
                    self.word_guessed.replace(self.word_guessed[index], self.guess)

                else :

                    pass

        else :

            print(f"Sorry, {self.guess} is not in the word. Try again.")

            self.num_lives-= 1

            print(f"Sorry, {self.guess} is not in the word.")

            print(f"You have {self.num_lives} lives left.")

        self.num_letters-=1

        return self.guess
    
    def ask_for_input(self) :

        '''
        method that asks the user for the input and makes sure it is a valid input

        The method asks the user for an input and checks that it is indeed a single alphabetical character, if not then another
        prompt to input a letter will appear

        Within the while loop and the if statement there is a check if the letter has already been guessed and will print a message 
        informing the user that the letter has already been tried
        
        every guess will be added to the list of guesses
        
        '''

        self.guess = input("Guess a letter:")

        while len(self.guess) != 1 or self.guess.isalpha() == False:

            print("Invalid letter. Please, enter a single alphabetical character.")

            self.guess = input("Guess a letter:")
            
            if self.guess.isalpha() == True and len(self.guess) == 1:
                if self.guess in self.list_of_guesses :
                    print("You already tried that letter!")
                
                else :
                    break

        self.list_of_guesses.append(self.guess)

        return self.check_guess(self.guess)


def play_game(word_list):

    num_lives = 5

    game = Hangman(word_list, num_lives) #creating an instance of the class

    while True :

        if num_lives==0 :
            print('You lost!')
        
        else :

            if game.num_letters > 0 :

                game.ask_for_input()  #calling the method within the Hangman class

            else :
                
                print('Congratulations. You won the game!')

                break

play_game(word_list)