import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# # print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# first = []
# random.shuffle(first)
# second = []
# random.shuffle(second)
# third = []
# random.shuffle(third)
# # generating random letters using choice random
# # storing it in a list called focus
#
# for number in range (nr_letters):
#     password = random.choice(letters)
#     first.append(password)
#
#
# # symbols
# for number in range (nr_symbols):
#     password = random.choice(symbols)
#     second.append(password)


#  for numbers
# for number in range (nr_numbers):
#     password = random.choice(numbers)
#     third.append(password)
#
# # output with all the random symbols,numbers and alphabets printed without space
# print(*first,*second,*third, sep="")
# together =[]
# together = first + second +third
# random.shuffle(together)
# print(together)
# # note: instead of using the append function we can say;
# # we declare a variable: passord = ""
# # then in the for loop: password + random.choice(numbers) or password += random.choice(numbers)
# # do a string concatenation
# n = 10
# hard_way = "12BD001928"
# hard_password = ""
# for i in range(n):
#     password = random.choice(hard_way)
#     hard_password = hard_password + password
# print(hard_password)
# the secret is concatenation
#Step 1



# Hangman program
word_list = ["aardvark", "baboon", "camel"]
display = []
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


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# chosen_word = random.choice(word_list)
# for _ in chosen_word:
#     display += "-"
# end_of_game = False
# while not end_of_game:
#     print(chosen_word)
#     guess = input("guess a letter ").lower()
#
#     # put the dashes into the list
#
#
#     # we associate each number of len(chosen_word) to replace the letters gotten right
#     for number in range(len(chosen_word)):
#         letter = chosen_word[number]
#         if letter == guess:
#             display[number] = letter
#     print(f"{' '.join(display)}")
#
#     if "-" not in display:
#         end_of_game = True
#
#
#
group = {'call': 'value2'}
for key in group:
    print(group[key])