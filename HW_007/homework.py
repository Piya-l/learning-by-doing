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

# Tuesday 28 Feb 2012
# Wednesday 29 Feb 2012
# Thursday 1 Mar 2012
# Sunday 1 Apr 2012
# Monday 1 Apr 2013
# Monday 2 Jan 2012
# Sunday 1 Jan 2012
# Saturday 31 Dec 2011
# Wednesday 30 Nov 2011
# Tuesday 30 Nov 2010
# Monday 28 Feb 2011
# Invalid year, month, or day!
# Invalid year, month, or day!    