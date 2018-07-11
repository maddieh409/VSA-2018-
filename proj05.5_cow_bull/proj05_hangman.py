# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random


    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

# your code begins here!
wordlist = load_words()
empty = []# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program

# your code begins here!
wordlist = load_words()
empty = []
word = choose_word(wordlist)
stop = 0
for letter in word:
    empty.append(letter)
worde = ["_"] * len(empty)
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print "Welcome to Tyler and Abhi's Hangman Game!"
length = len(word)
difficulty = raw_input("Select a difficulty. (easy, normal, hard, or extreme)")
if difficulty == "easy":
    a = 11
elif difficulty == "normal":
    a = 9
elif difficulty == "hard":
    a = 7
elif difficulty == "extreme":
    a = 5
else:
    a = 3
    difficulty = "impossible"
print "Your difficulty is " + difficulty + "."
print "I am thinking of a word that is " + str(length) + " letters long."
while stop == 0:
    print(worde)
    print "You have " + str(a) + " incorrect guesses left."
    print "Available letters: " + str(abc)
    guess = raw_input("Please guess a letter.")
    abc.remove(guess)
    correct = False
    counter = 0
    for letter in word:
        if guess == letter:
            worde[counter] = guess
            correct = True
            print "Correct!"
        counter = counter + 1
    if correct == False:
            a = a - 1
            print "That's incorrect!"
    if empty == worde:
        stop = 1
        print "You guessed the word!"
        print "The word was " + word + "!"
    if a == 0:
        stop = 1
        print "You lost!"
        print "The word was " + word + "!"