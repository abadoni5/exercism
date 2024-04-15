"""
Meetup day calculator.

This module provides a function `meetup` for calculating meetup days based on the year, month, number, and weekday provided.

Approach:
- The `meetup` function takes the year, month, number (e.g., 'first', 'second'), and weekday (e.g., 'Monday', 'Tuesday') as input.
- It maps weekdays and numbers to corresponding numbers and indices for easier manipulation.
- For 'teenth', it iterates through the teenth days of the given weekday in the specified month and returns the first valid date found.
- For other number cases, it iterates through the month's days of the given weekday and returns the date corresponding to the specified number.
- Custom exceptions are used to handle errors like invalid dates or missing teenth days.

"""

from datetime import date
import calendar


class MeetupDayException(Exception):
    """Custom exception for when the meetup day is not valid.

    Attributes:
        day -- the day that is causing the error
        message -- explanation of the error
    """
    
    def __init__(self, err, message="That day does not exist."):
        self.err = err
        self.message = message
        return super().__init__(self.message)


def meetup(year, month, number, weekday):

    days_to_numbers = {'Monday'   :0,
                       'Tuesday'  :1,
                       'Wednesday':2,
                       'Thursday' :3,
                       'Friday'   :4,
                       'Saturday' :5,
                       'Sunday'   :6}

    number_to_week = {'first'   :0,
                      'second'   :1,
                      'third'   :2,
                      'fourth'   :3,
                      'fifth'   :4,
                      'last'  :-1}

    day_number = days_to_numbers[weekday]
    number = number.lower()

    if number == 'teenth':
        teenth_cal = calendar.Calendar()
        teenths = sorted(item for item in teenth_cal.itermonthdays4(year, month)
                         if item[2] in range(13, 20) and item[3] == day_number)

        if teenths:
            return date(*teenths[0][:3])
        else:
            raise MeetupDayException(f'Teenth not found for {weekday}')

    else:
        week_number = number_to_week[number]
        remaining_cal = calendar.Calendar()
        cadidates = sorted(item for item in remaining_cal.itermonthdays4(year, month)
                           if item[1] == month and item[3] == day_number)

        try:
            return date(*cadidates[week_number][:3])
        except ValueError as err:
            raise MeetupDayException(err) from None
        except IndexError as err:
            raise MeetupDayException(err) from None
