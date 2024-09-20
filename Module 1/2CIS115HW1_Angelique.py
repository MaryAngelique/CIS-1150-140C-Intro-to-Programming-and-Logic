### For all questions, you should print the answer in the form of "The answer to question X is _"

### Question 1a-1d
## 1a Calculate and print the sum of 284 plus 965
var1a = 284
var2a = 965
print("The answer to question 1a is: " + str(var1a + var2a))
## 1b Calculate and print the difference of 473 minus 584
var1b = 473
var2b = 584
print("The answer to question 1b is: " + str(var1b - var2b))
## 1c Calculate and print the product of 47 times 23
var1c = 47
var2c = 23
print("The answer to question 1c is: " + str(var1c * var2c))
## 1d Calculate and print the quotient of 586 divided by 32
var1d = 586
var2d = 32
print("The answer to question 1d is: " + str(var1d / var2d))

### Question 2a-2b
## 2a Calculate and print the remainder of 586 divided by 32
var2a = 586 % 32
print("The answer to question 2a is: " + str(var2a))
## 2b Calculate and print the result of 4 raised to the 3rd power
var2b = 4 ** 3
print("The answer to question 2b is: " + str(var2b))

### Question 3a-3d
## 3a Calculate and print the sum of 5.83 and 273.34
var3a = 5.83 + 273.34
print("The answer to question 3a is: " + str(var3a))
# 3b Calculate and print the difference of 83.42 minus 57.332
var3b = 83.42 - 57.332
print("The answer to question 3b is: " + str(var3b))
## 3c Calculate and print the product of 3.9 times 11.4
var3c = 3.9 * 11.4
print("The answer to question 3c is: " + str(var3c))

## 3d Calculate and print the quotient of 1043.7 divided by 26.2
var3d = 1043.7 / 26.2
print("The answer to question 3d is: " + str(var3d))

### Question 4a-4b
## 4a Calculate and print the remainder of 742.5 divided by 23.94
var4a = 742.5 % 23.94
print("The answer to question 4a is: " + str(var4a))

## 4b Calculate and print the result of 6.8 raised to the 4.11th power
var4b = 6.8 ** 4.11
print("The answer to question 4b is: " + str(var4b))

### Question 5
### Add the following numbers together by casting the strings num1-3, then store the result in a variable called sum
### Print the sum as usual.
num1 = "5.55"
num2 = "3.33"
num3 = "9.01"
print("The answer to question 5 is: " + str(float(num1) + float(num2) + float(num3)))

### Question 6
### Swap the values of stringa and stringb, without manually typing out strings.  As a hint, you can use a temporary variable.
stringa = "This is stringb "
stringb = "This is stringa "
print("The answer to question 6 is: " + str(stringa) + str(stringb))

# your code here
# temporary variable
temp = stringa
stringa = stringb
stringb = temp

print(stringa)
print(stringb)
