#--------Get data--------

from time import localtime as lt
from pyscript import document
output_div = document.querySelector("#outputField")

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

def run(event):

    global year
    global month
    global day
    global document
    global output_div

    dayErrorOut = document.querySelector("#dayError")
    monErrorOut = document.querySelector("#monError")
    yearErrorOut = document.querySelector("#yearError")

    year = lt().tm_year
    month = lt().tm_mon
    day = lt().tm_mday

    getDay()
    
    try:
        bdayBox = document.querySelector("#dayIn")
        bday = int(bdayBox.value)
        dayErrorOut.innerText = ""
    except ValueError:
        dayErrorOut.innerText = "Please input a valid integer"
        output_div.innerText = ""
    else:
        if bday not in range (1, 32):
            dayErrorOut.innerText = "Please input a valid day"
            output_div.innerText = ""
        elif (birth_year == year) and (bmon == month) and (bday > day):
            dayErrorOut.innerText = "That day is yet to come!"
            output_div.innerText = ""

    try:
        bmonBox = document.querySelector("#monIn")
        bmon = int(bmonBox.value)
        monErrorOut.innerText = ""
    except ValueError:
        monErrorOut.innerText = "Please input a valid integer"
        output_div.innerText = ""
    else:
        if bmon < 0 or bmon > 12:
            monErrorOut.innerText = "Please input a valid month"
            output_div.innerText = ""
        elif (birth_year == year) and (bmon > month):
            monErrorOut.innerText = "That month is yet to come!"
            output_div.innerText = ""

    try:
        byearBox = document.querySelector("#yearIn")
        birth_year = int(byearBox.value)
        yearErrorOut.innerText = ""
    except ValueError:
        yearErrorOut.innerText = "Please input a valid integer"
        output_div.innerText = ""
    else:
        if birth_year not in range((year - 150), (year + 1)):
            yearErrorOut.innerText = "Please input a valid year"
            output_div.innerText = ""

    try:
        yearAge = year - birth_year
    except UnboundLocalError:
        return
    try:
        monAge = month - bmon
    except UnboundLocalError:
        return
    try:
        dayAge = day - bday
    except UnboundLocalError:
        return

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
    if (bmon == month) and ((dayAge * -1) in range(1, 15)):
        bdaySoon = True
        wait = dayAge * -1
        weekWait = wait / 7
        weekWaitFloored = int(round(weekWait, 0))
        if wait >= 7:
            happyBday = f'Your birthday is in (roughly) {weekWaitFloored} week(s)!'
        else:
            happyBday = f'Your birthday is in {wait} days!'
    else:
        bdaySoon = False

    #Tell the user how old they are :)
    
    if bdaySoon is True:
        actualAge = f'{actualAge}\n{happyBday}'
    output_div.innerText = actualAge
