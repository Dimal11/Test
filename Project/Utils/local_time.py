import time
from datetime import date


class LocalTime:
    def __init__(self):
        self.time = time.localtime()

    def get_date_time(self):
        return time.strftime('%B %d, %Y %I:%M %p', self.time)

    def get_date(self):
        return time.strftime('%m/%d/%Y', self.time)

    def get_month(self):
        return time.strftime('%m', self.time)

    def get_day(self):
        return time.strftime('%d', self.time)

    def get_year(self):
        return int(time.strftime('%Y', self.time))

    def get_closest_leap_year(self):
        year = int(time.strftime('%Y', self.time))
        previous_leap_year = year
        next_leap_year = year
        a = True
        while a:
            if next_leap_year % 4 == 0 and next_leap_year % 100 != 0 or next_leap_year % 400 == 0:
                a = False
            else:
                next_leap_year += 1
        a = True
        while a:
            if previous_leap_year % 4 == 0 and previous_leap_year % 100 != 0 or previous_leap_year % 400 == 0:
                a = False
            else:
                previous_leap_year -= 1

        current_date = date.today()
        previous_date = date(previous_leap_year, 2, 29)
        next_date = date(next_leap_year, 2, 29)

        if previous_leap_year == year == next_leap_year:
            return year

        elif abs(current_date - previous_date).days > abs(next_date - current_date).days:
            return next_leap_year

        else:
            return previous_leap_year
