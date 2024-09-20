'''
You want to ride a roller coaster.  Take a non-negative integer as input for age.
If the age is less than 12, print "You are too young to ride this roller coaster".
If the age is greater than or equal to 12, take in another non-negative integer as input, this is for height (in inches).
If the height is less than 54, print "You are too short for this roller coaster".
If the height is greater than or equal to 54, print "Welcome aboard".
'''

num = int(input("Enter your age: "))

if num < 12:
    print("You are too young to ride this rollercoaster")
else:
    height = int(input("Enter your height: "))
    if height < 54:
        print("You are too short for this rollercoaster")
    else:
        print("Welcome aboard")