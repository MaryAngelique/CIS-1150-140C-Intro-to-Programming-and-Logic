'''
### Submit a Python file for each question, with the name CIS115_HW2_Q*_yourname.py, where the * is the number of the question
### For example, the answer to Question 4 should be submitted as CIS115_HW2_Q4_yourname.py.

### Question 1
### Ask the user to input a number.  If this number is greater than 100 print "big number".  If it is not print "small number"

### Question 2
### Ask the user to input a name.  If the name is "Bob" print "Welcome home Bob".  If the name is not "Bob" print "You are not Bob get out!"

### Question 3
### Ask the user to input an integer.  Assume the number is positive.  If the number is less than 1000 print "3 digits or less".  If the number is equal to 1000 print "the number is 1000".
### If the number is greater than 1000 print "4 digits or more"

### Question 4
### Ask the user to input an integer.  Assume the number is positive and nonzero.  If the number is 1-9, print "1 digit".  If the number is 10-99 print "2 digits".
### If the number is 100-999 print "3 digits". If the number is 1000-9999 print "4 digits".  If the number is 10000-99999 print "5 digits".
### If the number is larger than 99999 print "too many digits".

### Question 5
### Take the answer to question 4, and add additional code to it.  If the number is a single digit, print whether it is odd or even.  If the number is 10-99, print whether it is a multiple of 5.
### If the number is 100-999, print whether it a multiple of 10.  If the number is 1000-9999, print whether the number is divisible by 111.
### If the number is larger than 10000-99999, print whether it is divisible by 3333.  If the number is larger than 99999, print whether it is divisible by 100000.

### Question 6
### Ask the user to input 1 number, called temperature.  If the temperature is between 65 and 75, inclusive, print "The weather is comfortable".
### If the temperature is greater than or equal to 55, but less than 65, print "the weather is cool but fine"
### If the temperature is greater than or equal to 45, but less than 55, print "the weather is getting chillier"
### If the temperature is greater than or equal to 30, but less than 45, print "the weather is getting cold"
### If the temperature is less than 30, print "the weather is cold"
### If the temperature is greater than 75 but less than or equal to 85, print "the weather is getting warmer"
### If the temperature is greater than 85, ask the user to input a new number, called humidity.
### If the temperature is greater than 85, but less than 95, and the humidity is less than 60, print "the weather is very warm but tolerable"
### If the temperature is greater than 85, but less than 95, and the humidity is greater than 60, print "The weather is very warm and humid"
### If the temperature is greater or equal to 95, and the humidity is less than 60, print "the weather is hot"
### If the temperature is greater or equal to 95, and the humidity greater than 60, print "the weather is hot and humid"
'''

temperature = int(input("Enter a temperature: "))

if temperature >= 65 and temperature <= 75:
    print("The weather is comfortable")
elif temperature >= 55 and temperature < 65:
    print("The weather is cool but fine")
elif temperature >= 45 and temperature < 55:
    print("The weather is getting chillier")
elif temperature >= 30 and temperature < 45:
    print("The weather is getting cold")
elif temperature < 30:
    print("The weather is cold")
elif temperature >= 75 and temperature <= 85:
    print("The weather is getting warmer")
else:
    humidity = int(input("Enter a humidity level: "))
    if temperature >= 85 and temperature < 95 and humidity < 60:
        print("The weather is very warm but tolerable")
    elif temperature >= 85 and temperature < 95 and humidity > 60:
        print("The weather is very warm and humid")
    elif temperature >= 95 and humidity < 60:
        print("The weather is hot")
    elif temperature >= 95 and humidity > 60:
        print("The weather is hot and humid")