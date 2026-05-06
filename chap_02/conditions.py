# Exercise 1: Rewrite your pay computation to give the employee 1.5 times 
# the hourly rate for hours worked above 40 hours.


# Prompt user for input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Check for overtime
if hours > 40:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

# Output result
print("Pay:", pay)