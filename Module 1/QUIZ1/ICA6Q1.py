'''
Q1 10 points
Type in a name.  This name should be letters only, all lowercase

If the name starts with the letters a-h, print "go to the left line"
If the name starts with the letters i-p, print "go to the middle line"
If the name starts with the letters q-z, print "go to the right line"
'''

name = input("Enter a name (lowercase letters only): ")

first_letter = name[0]

if first_letter in 'abcdefgh':
    print("go to the left line")
elif first_letter in 'ijklmnop':
    print("go to the middle line")
elif first_letter in 'qrstuvwxyz':
    print("go to the right line")
else:
    print("Invalid input. Please enter a name starting with a lowercase letter.")