day = 0
month = 1
year = 1901
dayIndex = 1
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
sundays = 0

while year < 2001:
    day += 1
    dayIndex += 1
    if dayIndex > 6:
        dayIndex = 0
    if month == 1:
        if day > 31:
            day = 1
            month += 1
        
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                day = 1
                month += 1
        else:
            if day > 28:
                day = 1
                month += 1
        
    elif month == 3:
        if day > 31:
            day = 1
            month += 1
    elif month == 4:
        if day > 30:
            day = 1
            month += 1
    elif month == 5:
        if day > 31:
            day = 1
            month += 1
    elif month == 6:
        if day > 30:
            day = 1
            month += 1
    elif month == 7:
        if day > 31:
            day = 1
            month += 1
    elif month == 8:
        if day > 31:
            day = 1
            month += 1
    elif month == 9:
        if day > 30:
            day = 1
            month += 1
    elif month == 10:
        if day > 31:
            day = 1
            month += 1
    elif month == 11:
        if day > 30:
            day = 1
            month += 1
    elif month == 12:
        if day > 31:
            day = 1
            month += 1
    if month > 12:
        month = 1
        year += 1
    if day == 1 and dayIndex == 0:
        sundays += 1
    print(day, month, year, days[dayIndex])
            
print(sundays)
            
    
    