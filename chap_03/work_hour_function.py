import yaml
config = yaml.safe_load(open("/Users/ruturajmokashi/Python Course/day_03/config.yaml", encoding="utf-8"))

total_hours = config['work_config']['hour']
overtime_rate = config['work_config']['overtime_rate']


#Option 3 (The best & professional)

def compute_pay3(hours,rate):
    if hours > total_hours:
        overtime = hours - total_hours
        pay = (total_hours * rate) + (overtime * rate * overtime_rate)
    else:
        pay = hours * rate
    return pay

hours = float(input ('Enter Hours'))
rate = float(input ('Enter Rate'))

print(compute_pay3(hours,rate))

#Option 1

"""

def compute_pay1(hours,rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    return pay

print(compute_pay1(45, 10)) 

"""
    
#Option 2

"""

def compute_pay2(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    return pay

h = 45
r = 10

p = compute_pay2(h, r)
print("Pay:", p)

"""







