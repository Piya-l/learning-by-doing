class MyDate:
    pass    

# Test cases
d1 = MyDate(2012, 2, 28)
print(d1.toString())
print(d1.nextDay().toString())
print(d1.nextDay().toString())
print(d1.nextMonth().toString())
print(d1.nextYear().toString())

d2 = MyDate(2012, 1, 2)
print(d2.toString())
print(d2.previousDay().toString())
print(d2.previousDay().toString())
print(d2.previousMonth().toString())
print(d2.previousYear().toString())

d3 = MyDate(2012, 2, 29)
print(d3.previousYear().toString())

# Invalid date examples
try:
    d4 = MyDate(2099, 11, 31)
except ValueError as e:
    print(e)

try:
    d5 = MyDate(2011, 2, 29)
except ValueError as e:
    print(e)
