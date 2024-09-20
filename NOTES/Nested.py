'''
Let’s say we have a more complex scenario:
• The speed limit is 65
• If the cop is in a bad mood, and you are speeding, he will pull you
over no matter what
• If the cop is in a good mood, he will now give you a warning as long as
you aren’t going faster than 75
• What does this look like?
'''

speed = int(input("How fast were you going? "))
happycop = bool(input("Is the cop in a good mood? "))
print("Is the cop in a good mood? " + str(happycop))

if speed <= 65:
    print("You are speeding!")
else:
    if happycop:
        if speed <= 75:
            print("You're getting a warning!")
        else:
            print("Here's a ticket")
    else:
        print("Here's a ticket")
    