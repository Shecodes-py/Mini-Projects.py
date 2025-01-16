"A Short Program: Guess the Number"
import random

name = input('Type in your name here:')
while True:
    print('Hello, ', name, 'Ready to Guess The Number? Press 1 to Start and 2 to Exit')
    guess = random.randint(1, 100)
    try:
        response = int(input())
        if response == 1:
            no_of_trials = 5
            trial_count = 0
            print('I am thinking of a number between 1 and 100.')
            print('Take a guess', name, '. You have', no_of_trials, 'trials')

            while True:
                 try:
                    user_input = int(input())
                    trial_count += 1
                    no_of_trials -= 1
                    if guess < user_input <= 100 and no_of_trials == 0:
                        print('Your guess is too high', name)
                        print('Sorry', name, '. The number I was thinking of was', str(guess))
                        break
                    elif guess > user_input >= 1 and no_of_trials == 0:
                        print('Your guess is too low', name)
                        print('Sorry', name, '. The number I was thinking of was', str(guess))
                        break
                    if guess < user_input <= 100:
                        print('Your guess is too high', name)
                        print('Take a guess.', 'You have', str(no_of_trials), 'left!')
                    elif guess > user_input >= 1:
                        print('Your guess is too low', name)
                        print('Take a guess.', 'You have', str(no_of_trials), 'left!')
                    elif user_input == guess:
                        print('Good job!', name, ' You guessed my number in', str(trial_count), 'guesses!')
                        break
                    elif user_input > 100 or user_input < 1:
                        print('Value entered not valid, pick a number between 1-30')
                 except ValueError:
                      print('Value entered not valid, Take a guess')
        elif response == 2:
            print('Game Over')
            break
        elif response != 1 or response != 2:
                    print('Invalid Response')
    except ValueError:
           print('Value entered not valid.')
           
# scores

def getAverageScore(scores):
    total=0
    for item in scores:
        total += item
    average = total/len(scores)
    return average

# print the average
def printAverage(average, name):
     print (name,", Your average score is",average)