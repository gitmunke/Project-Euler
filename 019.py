# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day_counter = 2 #tuesday, monday is 1 sunday is 7

def days_in_month(mon):
    mon = int(mon)
    if mon <= 0:
        return
    if mon > 12:
        return
    if mon == 2:
        return 28
    if mon == 9:
        return 30
    if mon == 4:
        return 30
    if mon == 6:
        return 30
    if mon == 11:
        return 30
    else:
        return 31

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

final_count = 0

for year in range(1901, 2001):
    for month in range(1,13):
        days = int(days_in_month(month))
        if leap_year(year):
            if month == 2:
                days = days + 1
        for w in range(days):            
            if day_counter > 7:
                day_counter = 1
            if w == 0:
                if day_counter == 7:
                    final_count += 1
                    print(year, month, day_counter)
            day_counter += 1

print(final_count)