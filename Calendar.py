#write a python program to display calender
import calendar
year=int(input('please enter the year:'))
month=int(input('please enter the month: '))
#get the month and year from the calender module
cal=calendar.month(year,month)
print(cal)


