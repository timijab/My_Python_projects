import random
import logo_bidder
# generates random numbers
# random_integers = random.randint(1, 20)
# print(random_integers)
#
# # random floating point number
# random_float = random.uniform(0, 5)
# print(random_float)
#
# random_floatpoint = random.random()
# print(random_floatpoint * 5)

# dice toss game
# name = input('Enter your name player')
# print(f'Welcome player {name} ')

# toss in a loop
# while name:
#     toss = input('Do you want to toss a coin Yes / No')
#     # if the player wants to play
#     if toss.lower() == 'yes':
#         random_integers = random.randint(1, 6)
#         # we take random integers from 1 to 6
#         print(random_integers)
#         # when the player gets a 6 he moves on, if he doesnt the player fails
#         if random_integers == 6:
#             print('Good toss!! \n you are out of your home!!')
#             toss_2 = input('toss second time!!! yes / No')
#             if toss_2.lower() == 'yes':
#                 random_integers_2 = random.randint(1, 6)
#                 if random_integers_2 == 6:
#                     print('you win congratulations')
#                 else:
#                     print('try again')
#                     break
#             else:
#                 break
#         else:
#             print(f'you got {random_integers}')
#             print('you are out')
#             break
#     if toss.lower() == 'no':
#         break

# names = input('give me everybodies name seperated by a comma \n')
# first = names.split(", ")
# print(f'{first[random.randint(0, len(first) - 1 )]} will pay this bill')

# change position of treasure
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# treasure = position.split(", ")
# selected_horizontal = int(treasure[0])
# selected_vertical = int(treasure[1])
# row1[selected_horizontal][selected_vertical].replace("⬜️", 'X')
# print(f"{row1}\n{row2}\n{row3}")

# Rock, Paper and scissors game
# rock = """"
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper =""""
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# game = [rock, paper, scissors]
# random_checks = random.randint(1, 3)
# choice = 0
# if random_checks == 1:
#     choice = rock
# elif random_checks == 2:
#     choice = paper
# if random_checks == 3:
#     choice = scissors
# number = int(input('Enter 1 for rock, Enter 2 for paper and Enter 3 for scissors '))
# if number == random_checks:
#     print('draw')
#     print(f'computer chose {choice} and you chose same!!')
#
# # user chooses rock and computer chose paper
# if number == 1 and random_checks == 2:
#     print(f'computer chose {choice}')
#     print(f'You chose rock \n {rock}')
#     print('you loose')
#
# # user chooses rock and computer chooses scissors
# if number == 1 and random_checks == 3:
#     print(f'Computer chose {choice}')
#     print(f'you chose rock \n {rock}')
#     print('You win')
#
# # User chooses paper and computer chooses rock
# if number == 2 and random_checks == 1:
#     print(f'computer choose paper{choice}')
#     print(f'you chose \n {paper}')
#     print('you win')
#
# # User chooses paper and computer choses  scissors
# if number == 2 and random_checks == 3:
#     print(f'computer chose {choice}')
#     print(f'you loose {paper}')
#
#
# # Code for paper needs optimization.
# # User chooses scissors and computer choses rock.
# if number == 3 and random_checks == 2:
#     print(f'computer chose {choice}')
#     print(f'you choose paper \n {scissors}')
#     print('you win')
#
# #   User chooses scissors and  chooses scissors.
# if number == 3 and random_checks == 1:
#     print(f'computer choose {choice}')
#     print(f'you choose paper \n {scissors}')
#     print('you lose')
import math
# height = input('enter the height if the classroom')
# classroom = height.split(" ")
# sum_of_class = 0

# Using the for loop function
# replicating sum function

# for i in classroom:
#     # sum_of_class is increased by adding the i to the previous vakue of sum of class room set to zero
#     sum_of_class = int(i) + sum_of_class
# print(sum_of_class)
# average_height = sum_of_class / len(classroom)
# print(math.ceil(average_height))
#
# # password generator
# # replicating the len function
#
# students_count = 0
# for students in classroom:
#     students_count += 1
# print(students_count)

# code to get the highest number in a list of numbers
# numbers = input('enter the heights of the students')
# heights = numbers.split(" ")
# highest = 0
# # max() gives the maximum number in a list
# # print(max(heights))
# # single = to a sign but double == is a check!!!
# for i in heights:
#     if int(i) > highest:
#         highest = int(i)
# print(highest)
# addition = 0
# for numbers in range(0, 101, 2):
#     addition += numbers
#     # or
#     # addition = addition + numbers
# # please note the accumulator is addition not numbers, we are storing each number in addition accumulator comes before numbers
# print(addition)

# fizzbuzz again

# for numbers in range(1, 101):
#     if numbers % 3 == 0 and numbers % 5 == 0:
#         print('Fizzbuzz')
#     if numbers % 3 == 0 and numbers % 5 != 0:
#         print('Fizz')
#     elif numbers % 5 == 0 and numbers % 3 != 0:
#         print('buzz')
#     elif numbers % 3 != 0 and numbers % 5 != 0:
#         print(numbers)
import math
import os
# program to determine the amount of paint on a wall
# height_wall = float(input('please enter the height of the wall in meters '))
# width_wall = float(input('please enter the weidth of the wall in meters '))
# def paint_calculation(height_wall, width_wall, coverage):
#     cover = height_wall * width_wall / coverage
#     print(f'You will need {math.ceil(cover)} cans of paint')
#
# paint_calculation(height_wall, width_wall, coverage = 5)

# prime number checker

# declaring a dictionary in python
# first_dictionary = {
#     'step_1':"I am awesome at this",
#     "step_2": "I will code everyday",
#     "step_3": "This is not a career change",
#     "step_4": "I will never giveup",
#     "step_5":"when there's a will there is a way"
# }
# adding to a dictionary
# first_dictionary["added_sub"] = 'I am awesome with God with me'
#
#
# first_dictionary["step_2"] = "changed"
# print(first_dictionary)
# for key in first_dictionary:
#     print(key)
#     print(first_dictionary[key])

# dictionaries
# student_scores = { "Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74,"Neville": 62,}
# student_grades = {}
#
# for key in student_scores:
#     student_grades[key] = student_scores[key]
#     # remember to obtain the element in a key we access using dict_name[key] = "" or any datatype
#     if 90 <= student_grades[key] <= 100:
#         student_grades[key] = 'outstanding'
#     elif 80 <= student_grades[key] < 90:
#         student_grades[key] = 'exceeded expectations'
#     elif 70 <= student_grades[key] < 80:
#         student_grades[key] = 'Acceptable'
#     else:
#         student_grades[key] = 'Failed'
# print(student_grades)

# Nested dictionary with list datatype
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country":country, "visits": visits, "cities": cities,
#                        })
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#
# print(travel_log)

# This function clears the screen
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



chosen_bid = []
common = True
largest_bid = 0
print(logo_bidder.logo)
while common:
    name = input('Enter your name ')
    bid  = float(input('place your bid in $'))
    clearConsole()
    def bid_compiler(name_bidder, bid_amount):
        chosen_bid.append({name: bid_amount})
    bid_compiler(name_bidder=name, bid_amount=bid)
    end_of_bid = input('Is there another bidder ')
    if end_of_bid.lower() == 'no':
        common = False
    elif end_of_bid.lower() == 'yes':
        common = True
# this code checks the list to obtain the value of the keys using the name of the dictionary and the key to access the value. e,g group[key]
for groups in chosen_bid:
    for key in groups:
        if groups[key] > largest_bid:
            largest_bid = groups[key]
            name_bidder = key
print(f'{name_bidder} won this Bid with ${largest_bid}')