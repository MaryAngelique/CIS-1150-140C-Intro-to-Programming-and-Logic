
# •Write a Python File justright_yourname.py that takes a number as input, and prints 3 different things depending on the number printed.
num = int(input("Enter a number: "))
# •If the number is <60, print “too low”
if num <  60:
    print("too low")
# •If the number is >=60 and <=80, print “just right”
if num >= 60 and num <= 80:
    print("just right")
# •If the number is >80 print “too high”
if num > 80:
    print("too high")
    
# •If the number is too low or too high, ask the user to input a new number, and print whether or not the new number is “just right”
if num < 60 or num > 80:
    new_num = int(input("Enter a new number: "))
    if new_num >= 60 and new_num <= 80:
        print("just right")

# •Submit this file to Moodle when you are done.

# while loop that asks the user to give a number and will return one of the 3 conditions and will ask them infinitely
''''
while True:
    num = int(input("Enter a number: "))
    if num < 60:
        print("too low")
    elif num >= 60 and num <= 80:
        print("just right")
    elif num > 80:
        print("too high")
    else:
        break
'''


