#--------Get data--------

from time import localtime as lt
from pyscript import document
output_div = document.querySelector("#outputField")

#-----------Prep---------

def getDay():

    global leap
    leap = 'false'
    global monDays
    if month in (1, 3, 5, 7, 8, 10, 12):
        monDays = 31

    if month == 2:
        leap = (year - 2000) / 4
        if not isinstance(leap, int):
            monDays = 28
            leap = 'false'
        else:
            monDays = 29
            leap = 'true'

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

    dayErrorVar = document.querySelector(#dayError)
    monErrorVar = document.querySelector(#monError)
    yearErrorVar = document.querySelector(#yearError)

    year = lt().tm_year
    month = lt().tm_mon
    day = lt().tm_mday

    getDay()
    
    try:
        bdayBox = document.querySelector("#dayIn")
        bday = int(bdayBox.value)
    except ValueError:
        dayErrorVar.innerText = "Please input a valid integer"
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
