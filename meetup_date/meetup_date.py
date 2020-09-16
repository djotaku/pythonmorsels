from datetime import date


def meetup_date(year, month, nth=4, weekday=3):
    """Given a year and month, return the day of the month that is the fourth Thursday."""
    target_weekday = 0
    for day_of_month in range(1, 32):
        if date(year, month, day_of_month).weekday() == weekday:
            target_weekday = target_weekday + 1
        if target_weekday == nth:
            return date(year, month, day_of_month)


if __name__ == "__main__":
    date = meetup_date(2020, 9)
    print(date)