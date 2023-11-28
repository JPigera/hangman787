# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

So far I have written a programme which takes in a user input of a letter from the user. Then the code checks that it is a valid user input and then checks if it is one of the letters of a random word from a set.
 
Most of the code is within a class called Hangman. Hangman contains two functions. The first one  "ask_for_input()"  asks the user for an input and makes sure that it is a valid input, then at the end of the function the second function is called. The second function is the check guess function "check_guess()". This function is used to tell the user if their guess was correct and will add their guess to a list of guesses. If the guess was wrong a message will be produced that the guess was wrong and a life will be taken from their lives.

This has been a useful project to implement the skills I have used thus far on the AI core course. It has also helped contextualise the tools that I have learnt and has shown the benefit of utilizing them.