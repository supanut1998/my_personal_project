# project hangman_game 

# import packages and modules that use in this project : random, material.py 
import random
from material import logo, stages, word_list 

#greeting 
print(f"{logo} \n\nWelcome to Hangman game!")

# rule 
rule = """ Rule of the game : 
guess the letter to correct the given word.
you have 6 lives. if you guess it all wrong you lose. """
print(rule)

# declare the neccessary variable 
# player life point
lives = 6 

#word that player have to guess 
chosen_word = random.choice(word_list)

# length of chosen word
word_length = len(chosen_word)

# blank that display to player 
blank_word = ["_" for _ in range(word_length)] 

# game trigger
end_of_game = False

#test code
print(chosen_word)

# game start
while not end_of_game : 
    # let player guess the word
    guess = input("Guess the letter: ")
    # check the if the guess is in the chosen_word or not 
    for position in range(word_length) : 

        # create chosen_word_letter that save letter value form chosen_word
        chosen_word_letter = chosen_word[position] 

        # compare temp letter from chosen_word with player guess letter
        if guess == chosen_word_letter : 

            # replace _ with guess value in list blank_word
            blank_word[position] = guess
        
    # print the result 
    print(" ".join(blank_word))


    # if guess it wrong : decease health show stage 
    if guess not in chosen_word :
        print(f"{guess} is not in the word") 
        lives -= 1 
        if lives == 0 : 
            end_of_game = True 
            print("Mission Failed We'll Get Em Next Time ")

    # win condition 
    if "_" not in blank_word : 
        end_of_game = True
        print("Congratulation! You win the game")
    
    #show stage of hangman
    print(stages[lives])
    





