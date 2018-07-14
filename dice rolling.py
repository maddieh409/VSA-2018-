one_points = 0
two_points = 0
user_input = raw_input("How many times would you like to play? ")
for random in range(int(user_input)):
    if random < user_input:
        import random
        dice_number = int(random.randint(1, 6))
        print dice_number

        if dice_number == 1 or dice_number == 3 or dice_number == 5:
            one_points = one_points + 1
            print "Player one wins and now has", one_points, "point(s)"
        elif dice_number == 2 or dice_number == 4 or dice_number == 6:
            two_points = two_points + 1
            print "Player two wins and now has", two_points, "point(s)"
    elif random == user_input:
        if one_points >= two_points:
            difference = one_points - two_points
            print difference
        if one_points < two_points:
            difference = two_points - one_points
            print difference



