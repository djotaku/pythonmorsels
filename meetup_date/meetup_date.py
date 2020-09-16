from datetime import date


def meetup_date(year, month):
    """Given a year and month, return the day of the month that is the fourth Thursday."""
    thursdays = 0
    for day_of_month in range(1, 32):
        if date(year, month, day_of_month).weekday() == 3:
            thursdays = thursdays + 1
        if thursdays == 4:
            return date(year, month, day_of_month)


if __name__ == "__main__":
    date = meetup_date(2020, 9)
    print(date)