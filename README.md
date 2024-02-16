# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

I have written a programme that takes in user input of a letter from the user. Then the code checks that it is a valid user input and then checks if it is one of the letters of a random word from a set.

![image](https://github.com/JPigera/hangman787/assets/135263152/c96ccacb-4677-4871-b71c-f24d9bd11df9)

 
Most of the code is within a class called Hangman. Hangman contains two functions. The first one  "ask_for_input()"  asks the user for input and makes sure that it is a valid input, then at the end of the function, the second function is called. The second function is the check guess function "check_guess()". This function is used to tell the user if their guess is correct and will add their guess to a list of guesses. If the guess was wrong a message will be produced that the guess was wrong and a life will be taken from their lives.

Then I created a function that contains the Hangman class and will call the class' ask for input method to play the game.

![image](https://github.com/JPigera/hangman787/assets/135263152/2d5e9707-2d05-4a2b-987a-0972d1d18f49)


This has been a useful project to implement the skills I have used thus far in the AI core course. It has also helped contextualize the tools that I have learned and has shown the benefit of utilizing them.
