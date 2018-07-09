# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.
#
# # Part II:
# # This program asks the user for his/her name and birth month.
# # Then, it prints a sentence that says the number of days and months until their birthday
#
#
# # If you complete extensions, describe your extensions here!
# print "Hello world!" + "cat"
# print 5 + 3
# #var name           input from user
# user_age = raw_input("Enter your age: ")
# print "you are " + user_age + " years old"
# print int(user_age) +10
# #var name              input from user
# user_name = raw_input("Name: ")
# user_grade = raw_input("What is your grade? ")
# print "Maddie, you will graduate in", 12 - int(user_grade), "year(s)"
# user_birthmonth = raw_input("When is your birthmonth? ")
# print int(user_birthmonth)
# user_birthdate = raw_input ("When is your birthdate? ")
# print user_birthmonth, user_birthdate = raw_input("When is your birthday? ")
#
# current_month = raw_input("What is the current month? ")
# current_day = raw_input("What is the current day? ")
# user_birthmonth = raw_input("When is your birthmonth? ")
# user_birthdate = raw_input ("When is your birthdate? ")
# #
# # if user_birthmonth > 7:
# #     print int(user_birthmonth) - 7
# elif user_birthmonth == 7:
#     print int(user_birthmonth) - 7
# else:
#     print int(user_birthmonth) + 5

# if user_birthmonth == 2:
#     print (28 - int(user_birthdate)) + 9
# if user_birthmonth == 9 or user_birthmonth == 4 or user_birthmonth == 6 or user_birthmonth == 11:
#     print (30 - int(user_birthdate)) + 9
# else:
#     print (31 - int(user_birthdate)) + 9
#
# if user_birthmonth >= current_month:
#     print int(user_birthmonth) - int(current_month), "months until your birthday"
# else:
#     print 12 - int(current_month) + int(user_birthmonth), "months until your birthday"
#
# if user_birthdate >= current_day:
#     print int(user_birthdate) - int(current_day), "days until your birthday"
# else:
#     print 30 - int(current_day) - int(user_birthdate), "days until your birthday"
#     print 11 - int(current_month) - (user_birthmonth), "days until your birthday"

user_name = raw_input("What is your name?")


# str = str.lower(user_name)

print user_name[0:2].lower() + user_name[2].upper() + user_name[3:].lower()


