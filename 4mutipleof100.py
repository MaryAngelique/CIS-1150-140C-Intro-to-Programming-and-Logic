'''
Take a positive integer as an input.  If the number is less than 100, print “less than 100” and then print whether or not it is a multiple of 10.  If the number is greater than 100, print “greater than 100” and print whether or not it is a multiple of 100.
'''

num = int(input("Enter a positive integer: "))

if num < 100:
    print("less than 100")
    if num % 10 == 0:
        print(f"{num} is a multiple of 10")
    else:
        print(f"{num} is not a multiple of 10")
elif num > 100:
    print("greater than 100")
    if num % 100 == 0:
        print(f"{num} is a multiple of 100")
    else:
        print(f"{num} is not a multiple of 100")