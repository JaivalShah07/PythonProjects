import calendar

def cal(month, year):
    month1 = calendar.month(year, month)
    print(month1)

try:
    month = int(input('Enter the month no: '))
    year = int(input('Enter the year: '))
    cal(month, year)

except ValueError:
    print('Enter valid month or year in number.')
