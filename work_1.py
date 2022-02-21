
# program two
#
# price = float(input('what amount of food was bought ? $'))
# percentage = input('what percentage of tip do you wanna give ?')
# result = int(percentage) * price // 100
# print(f' Your bill is ${price + result} and your tip is ${result,2}')


# love calculator
# t = combined_strings.count('t')
# r = combined_strings.count('r')
# u = combined_strings.count('u')
# e = combined_strings.count('e')
# true = t + r + u + e
# l = combined_strings.count('l')
# o = combined_strings.count('o')
# v = combined_strings.count('v')
# e = combined_strings.count('e')
# love = l + o + v + e
# answer = true + love
# print(f'Your score is {answer}')
# if answer > 50:
#     print(f'You guys going through bread and butter')
#     print(f'{answer} wow what is a score!')
# else:
#     print('You guys go like coke and menthos')

# Treasure Island
print("""*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""".   |""")

treasure = print('Welcome to the treasure island, you will be required to make quality decisions to navigate to to get the treasure')
print('You start now !!')

game = input('Do you want to continue Yes/No \n')
while game.lower() == 'yes':
    first_step = input('Right or Left \n')
    if first_step.lower() == 'left':
        wait = input('Swim or wait \n')
        if wait.lower() == 'wait':
            door = input('What door is it red // blue // yellow ? \n')
            if door.lower() == 'yellow':
                print('You win!!! \n')
                print('Congratulation\n')
            elif door.lower() == 'blue':
                print('Eaten by beast \n')
                print('Game Over!! \n')
            else:
                print('Game Over')
        else:
            print('you fall into a hole \n')
            print('Game over!! \n')
    else:
        print('Fall into hole game over \n')
    end_game = input('Do you wish to continue yes or no \n')
    if end_game.lower() == 'no':
        break







