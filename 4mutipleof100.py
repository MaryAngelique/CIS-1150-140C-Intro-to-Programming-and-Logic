'''
Take a positive integer as an input.  If the number is less than 100, print “less than 100” and then print whether or not it is a multiple of 10.  If the number is greater than 100, print “greater than 100” and print whether or not it is a multiple of 100.
'''

if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    
    if num < 100:
        print("less than 100")
        print(num % 10 == 0)
    else:
        print("greater than 100")
        print(num % 100 == 0) 