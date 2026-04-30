#--------Get data--------

def run(event):
    from pyscript import document
    output_div = document.querySelector("#outputField")

    from time import localtime
    global year
    year = localtime().tm_year
    global month
    month = localtime().tm_mon
    global day
    day = localtime().tm_mday
    
    calc()

#-----------Prep---------

def getDay():
    global leap
    leap = 'false'
    global monDays
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        monDays = 31

    if month == 2:
        leap = (year - 2000) / 4
        leapCheck = int((year - 2000) / 4)
        if leap == leapCheck:
            leap = int(leap)
        if not isinstance(leap, int):
            monDays = 28
            leap = 'false'
        else:
            monDays = 29
            leap = 'true'

    if month == 4 or 6 or 9 or 11:
        monDays = 30
    print(f'Year: {year}')
    print(f'Month: {month}')
    print(f'Day: {day}')
    print(f'Leap: {leap}')
    print(f'This month has {monDays} days')

#--------Get user data----------

def calc():
    getDay()

    bdayBox = document.querySelector("#dayIn")
    bday = int(bdayBox.value)
    bmonBox = document.querySelector("#monIn")
    bmon = int(bmonBox.value)
    byearBox = document.querySelector("#yearIn")
    birth_year = int(byearBox.value)

    yearAge = year - birth_year
    monAge = month - bmon
    dayAge = day - bday

    #-Determine whether or not the month should be classed as before your birthday or after and doing maths to use that and output

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
        else:
            actMonth = (12 - bmon) + month
            actY = yearAge - 1
        if day > bday:
            actualAge = f'You are {actY} years, {actMonth} months and {dayAge} days old'
        else:
            month = bmon
            getDay()
            actualAge = f'You are {actY} years, {actMonth - 1} months and {((monDays - bday) + day) + 1} days old'


    #Tell the user how old they are :)

    output_div.innerText = actualAge
