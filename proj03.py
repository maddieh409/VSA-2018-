# Name:
# Date:

#
# """
# proj 03: Guessing Game
#
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. Keep the game going until the user types exit.
# Keep track of how many guesses the user has taken, and wh
#
# """
sum = 0
import random
answer = random.randint(1, 9)
number = 1

play = raw_input("say yes to play: ")
while play == "yes":
    while int(number) != int(answer):
        number = raw_input("Enter a number from 1-9, or exit to end the game: ")
        if str(number) == str("exit"):
            print "Game over"
            break
        if int(number) < int(answer):
            print "your number is too low!"
            sum = sum + 1
        if int(number) > int(answer):
            print "your number is too high!"
            sum = sum + 1
        if int(number) > 9:
            print "your number is invalid"
            sum = sum + 1
        if int(number) < 0:
            print "your number is invalid"
            sum = sum + 1
        if int(number) == int(answer):
            sum = sum + 1
            print "Congratulations you guessed my number! You used", int(sum), "guesses."
            play = raw_input("say yes to play: ")
            number = 0
            sum = 0
            answer = random.randint(1, 9)






