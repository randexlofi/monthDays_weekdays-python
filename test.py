from datetime import date
from calendar import monthrange

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# Input the year
year_inp = int(input('year > '))

# Check if month is between 1 or 12 (jan-dec)
month_inp = 0
while month_inp < 1 or month_inp > 12:
    month_inp = int(input('month > '))

# Check if the input day exists in the day length of the input month
month_days = monthrange(year_inp, month_inp)[1]
day_inp = 0
while day_inp < 1 or day_inp > month_days:
    day_inp = int(input('day > '))


date = date(day=day_inp, month=month_inp, year=year_inp)
index_of_week = date.weekday()
day_of_week = days[index_of_week]
month_name = months[date.month - 1]


print('Day: {}'.format(date.day))
print('Month: {} ({} days)'.format(month_name, month_days))
print('Year: {}'.format(date.year))
print('Week Day: {}'.format(day_of_week))