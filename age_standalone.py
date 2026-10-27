#--------Get data--------

from time import localtime
year = localtime().tm_year
month = localtime().tm_mon
day = localtime().tm_mday

bday = ''
bmon = ''
birth_year = ''

#-----------Prep---------

def getDay():
    global leap
    leap = False
    global monDays
    if month in (1, 3, 5, 7, 8, 10, 12):
        monDays = 31

    if month == 2:
        leap = (year - 2000) / 4
        if not isinstance(leap, int):
            monDays = 28
            leap = False
        else:
            monDays = 29
            leap = True

    if month in (4, 6, 9, 11):
        monDays = 30
    print(f'Year: {year}')
    print(f'Month: {month}')
    print(f'Day: {day}')
    print(f'Leap: {leap}')
    print(f'This month has {monDays} days')

#--------Get user data----------

getDay()
while birth_year == '':
    try:
        birth_year = int(input('Year? '))
    except ValueError:
        print('wtf? WHO EVEN WRITES THE YEAR IN WORDS???')
    else:
        if birth_year not in range((year - 150), (year + 1)):
            print('Please input a valid year')
            birth_year = ''
while bmon == '':
    try:
        bmon = int(input('Month? '))
    except ValueError:
        print('*sigh* NUMBERSSSSS!')
    else:
        if bmon < 0 or bmon > 12:
            print('Please input a valid month')
            bmon = ''
        elif (birth_year == year) and (bmon > month):
            print('That month is yet to come!')
            bmon = ''
while bday == '':
    try:
        bday = int(input('What day were you born on? '))
    except ValueError:
        print('Numbers please! (Make sure to just write the DAY not the full date)')
    else:
        if bday not in range (1, 32):
            print('Please input a valid day')
            bday = ''
        elif (birth_year == year) and (bmon == month) and (bday > day):
            print('That day is yet to come!')
            bday = ''
yearAge = year - birth_year
monAge = month - bmon
dayAge = day - bday

#-Determine whether or not the month should be classed as
#-before your birthday or after and doing
#-maths to use that and output the age

if month > bmon:
    if day > bday:
        actualAge = f'You are {yearAge} years, {monAge} months and {dayAge} days old'
    else:
        month = bmon
        getDay()
        actualAge = f'You are {yearAge} years, {monAge} months and {(monDays - bday) + day} days old'
else:
    if (12 - bmon) + month == 12:
        actMonth = 0
        actY = yearAge
        if day > bday:
            actualAge = f'You are {actY} years, {actMonth} months and {dayAge} days old'
        elif day == bday:
            actualAge = f'You are {actY} years, {actMonth} months and {dayAge} days old'
        else:
            actualAge = f'You are {actY - 1} years, 11 months and {((monDays - bday) + day) + 1} days old'
    else:
        actMonth = (12 - bmon) + month
        actY = yearAge - 1
        if day > bday:
            actualAge = f'You are {actY} years, {actMonth} months and {dayAge} days old'
        else:
            month = bmon
            getDay()
            actualAge = f'You are {actY} years, {actMonth - 1} months and {((monDays - bday) + day) + 1} days old'
if (bmon == month) and ((dayAge * -1) <= 14):
    wait = dayAge * -1
    weekWait = wait / 7
    weekWaitFloored = int(round(weekWait, 0))
    if wait >= 7:
        happyBday = f'Your birthday is in (roughly) {weekWaitFloored} week(s)!'
    elif wait > 1:
        happyBday = f'Your birthday is in {wait} day(s)!'
    elif wait == 0:
        happyBday = 'HAPPY BIRTHDAY!'
    else:
        happyBday = 'Your birthday is tomorrow!'

#-Tell the user how old they are :)

print(actualAge)
try:
    print(happyBday)
except NameError:
    happyBday = 0
