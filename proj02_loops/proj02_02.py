# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

#
# previous_number = 1
# current_number = 1
# next_number = 2
# num = raw_input("Enter number here")
#
# for num in range (0, 22):
#     print current_number
#     next_number = previous_number + current_number
#     previous_number = current_number
#     current_number = next_number

previous_number = 1
current_number = 1
number_of_fibnums = int(raw_input("Enter number here"))

for number_of_fibnums in range(number_of_fibnums):
    print current_number
    previous_number = current_number
    current_number = previous_number + current_number






