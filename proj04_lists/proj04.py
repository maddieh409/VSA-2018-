# # coding=utf-8
# # Name:
# # Date:
#
# var = ["a", "b"]
#
#
#
# """
# proj04
#
# practice with lists
#
# """
#
# #Part I
# #Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# print a[:5]

#and write a program that prints out all the elements of the list that are less than 5.
#
# number = int(raw_input("Enter a number."))
# for numbers in a:
#     if numbers < number:
#         print numbers

#
#
# #
# # #Part II
# # # Take two lists, say for example these two:
# b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # # and write a program that creates and prints a list that contains only the elements
# # # that are common between the lists (without duplicates).
# # # Make sure your program works on two lists of different sizes.
#
# counter = 0
#
# for item in b:
#     if item in c:
#         print item


# for numbers in c:
#     if numbers == numbers in b:
#         print numbers
#
#
#
#
#
#
# #Part III
# # Take a list, say for example this one:
# #
# d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# # # and write a program that replaces all “a” with “*”.
# #
# counter = 0
# old_name = "a"
# new_name = "a"
#
#
# for numbers in d:
#     old_name = "a"
#     new_name = "*"
#     if numbers == old_name:
#             d[counter] = new_name
#     counter = counter + 1
# print d
#
#
#
#
#
#
#
# #Part IV
# #Ask the user for a string, and print out whether this string is a palindrome or not.
check = True
empty_list = []
string = raw_input("Type a string in the space provided, to determine whether or not it is a palindrome: ")
string = string.lower()
for letters in string:
    empty_list.append(letters)
begin_counter = 0
end_counter = len(string) - 1

for items in range (len(string)/2):
    if string[begin_counter] == string[end_counter]:
        begin_counter = begin_counter + 1
        end_counter = end_counter - 1
    else:
        print "Your string is not a palindrome."
        check = False
        break
if check == True:
    print "Your string is a palindrome"


# if string[0] != string[-1]:
#     print "Your string is not a palindrome."
# else:
#         for item in string:
#             if :
#                 item == counter
#                 item[str(counter)] = string
#                 counter = counter + 1
#             elif counter == -1:
#                 item == counter
#                 item[str(counter)] = string
#                 counter = counter - 1
#                 print "Your string is a palindrome!"










