
class MyDate:
    pass    

# Test cases
d1 = MyDate(2012, 2, 28)
print(d1)             # Tuesday 28 Feb 2012
print(d1.nextDay())   # Wednesday 29 Feb 2012
print(d1.nextDay())   # Thursday 1 Mar 2012
print(d1.nextMonth()) # Sunday 1 Apr 2012
print(d1.nextYear())  # Monday 1 Apr 2013

d2 = MyDate(2012, 1, 2)
print(d2)                 # Monday 2 Jan 2012
print(d2.previousDay())   # Sunday 1 Jan 2012
print(d2.previousDay())   # Saturday 31 Dec 2011
print(d2.previousMonth()) # Wednesday 30 Nov 2011
print(d2.previousYear())  # Tuesday 30 Nov 2010

d3 = MyDate(2012, 2, 29)
print(d3.previousYear())  # Monday 28 Feb 2011

# Invalid date examples
try:
    d4 = MyDate(2099, 11, 31)  # Invalid date
except ValueError as e:
    print(e)

try:
    d5 = MyDate(2011, 2, 29)  # Invalid date
except ValueError as e:
    print(e)