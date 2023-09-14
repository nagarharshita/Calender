import calendar
y=int(input("Enter the required year: "))
m=1
print("\n   CALENDER ",y)
print()
#instance of TextCalender is to be created
#SUNDAY means that starting displaying from Sunday
c=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
#prmonth() is a function of the class that prints the calender for given month and year
    c.prmonth(y,i)
    i+=1
