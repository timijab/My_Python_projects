import random
logo = print(""""  __  .__                                                                                 
_/  |_|  |__   ____      ____  __ __   ____   ______ ______    _________    _____   ____  
\   __\  |  \_/ __ \    / ___\|  |  \_/ __ \ /  ___//  ___/   / ___\__  \  /     \_/ __ \ 
 |  | |   Y  \  ___/   / /_/  >  |  /\  ___/ \___ \ \___ \   / /_/  > __ \|  Y Y  \  ___/ 
 |__| |___|  /\___  >  \___  /|____/  \___  >____  >____  >  \___  (____  /__|_|  /\___  >
           \/     \/  /_____/             \/     \/     \/  /_____/     \/      \/     \/""")

print('Welcome to the Number guessing Game!')
print('I am thinking of a random number within the range 1 to 100')
num = random.randint(1, 100)
print(num)

game_life = input('\nChoose your difficulty level: Hard or easy ').lower()

choice = int(input('Enter your guess '))

def conditions():
    if num == choice:
        print(f'you guessed my number right {num} \nYou Won!!!!')
    elif choice > num:
        print("Too far above")
    elif choice != num  and choice > num - 10 :
        print("you are getting closer")
    elif choice < num:
        print( "Too far below the my number")
    elif choice < num - 10:
        print("You are getting closer")
conditions()

# bug we need to update choice on each loop
def end_of_game():
        if game_life == 'easy':
            i = 1
            while i < 10:
                global choice
                choice = int(input("Enter your guess "))
                conditions()
                print(f"You have {9-i} lives left ")
                i += 1
                if i == 10 and choice != num:
                    print('But you have exhausted your game life, Game over!!!')
                elif num == choice:
                    i = 11

        #     hard game-life gives a chance of five times
        elif game_life == 'hard':
            i = 1
            while i < 5:
                choice = int(input("Enter your guess "))
                conditions()
                print(f"You have {4 - i} lives left ")
                i += 1
                if i == 5 and choice != num:
                    print('But you have exhausted your game life, Game over!!!')
                elif num == choice:
                    i = 6
end_of_game()

