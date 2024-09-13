'''
Ask the user for 2 numbers.  One number should be the hours worked, and the other number should be their hourly pay rate.
•Your program should print how many hours are worked with regular pay, and how many hours worked are overtime (for hours above 40).
•Overtime pay should be 50% more than regular pay.
•Your program then calculate and print how much regular pay is made, and how much overtime pay is made, along with the total pay.
•Assume that the number of hours is a non-negative number.
'''

hours_worked = float(input("How many hours did you work? "))
hourly_pay_rate = float(input("What is your hourly pay rate? "))

regular_hours = min(hours_worked, 40)
overtime_hours = max(0, hours_worked - 40)

regular_pay = regular_hours * hourly_pay_rate
overtime_pay = overtime_hours * hourly_pay_rate * 1.5

total_pay = regular_pay + overtime_pay

print(f"You are working " + str(hours_worked) + " hours, with regular pay, and " + str(overtime_hours) + " hours with overtime pay.")
print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Total pay: ${total_pay:.2f}")