import random
import words
import Hangman

print(Hangman.logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = words.word_list
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
game_life  = 6

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(*display, sep= "")
previous = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter and see if it has been entered before

    for item in previous:
        if guess == item:
            repeat = 'you have entered this already, try another alphabet'
            print(repeat)
    previous += guess

    # to check entered guess position
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter



    if guess  not in chosen_word:
        game_life -= 1
        print(f'you guessed * {guess}')
        print('It is not in the keyword, you lose a life')
    #TODO-2: - If guess is not a letter in the chosen_word,

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif game_life == 0:
        end_of_game = True
        print('You lose')

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[game_life])