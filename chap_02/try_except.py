# Exercise 2: Rewrite your pay program using try and except so 
# that your program handles non-numeric input gracefully by printing 
# a message and exiting the program. The following shows two executions of the program:

try:
    # Take input and convert to float
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    # Pay calculation with overtime
    if hours > 40:
        regular_pay = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        pay = regular_pay + overtime
    else:
        pay = hours * rate

    print("Pay:", pay)

except:
    print("Error, please enter numeric input")