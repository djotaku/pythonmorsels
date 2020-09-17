from datetime import date


def meetup_date(year, month, nth=4, weekday=3):
    """Given a year and month, return the day of the month that is the fourth Thursday."""
    start = 0
    end = 0
    step = 0
    if nth > 0:
        start = 1
        end = 32
        step = 1
    else:
        start = 31
        end = 0
        step = -1
    target_weekday = 0
    for day_of_month in range(start, end, step):
        try:
            if date(year, month, day_of_month).weekday() == weekday:
                target_weekday = target_weekday + 1
            if target_weekday == abs(nth):
                return date(year, month, day_of_month)
        except:
            print("short month")


if __name__ == "__main__":
    date = meetup_date(2020, 2, -1)
    print(date)