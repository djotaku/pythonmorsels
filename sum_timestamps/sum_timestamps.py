import math


def figure_out_base_sixty(number: int) -> (int, int):
    """Figure out the next number up if I have more than 59 seconds or minutes."""
    if number > 59:
        return math.floor(number/60), number % 60
    else:
        return 0, number


def sum_timestamps(timestamps: list) -> str:
    """Accept a list of timestamps (in the format of MM:SS or HH:MM:SS) and return a timestamp that is the sum of all
    given times.

    :param timestamps: A list of timestamps.
    :type timestamps: list
    :returns: Timestamp sum of all times in the list.
    """
    split_time = [timestamp.split(':') for timestamp in timestamps]
    hours = []
    minutes = []
    seconds = []
    for timestamp in split_time:
        if len(timestamp) == 2:
            minutes.append(int(timestamp[0]))
            seconds.append(int(timestamp[1]))
        else:
            hours.append((int(timestamp[0])))
            minutes.append(int(timestamp[1]))
            seconds.append(int(timestamp[2]))
    total_hours_step_1 = sum(hours)
    total_minutes_step_1 = sum(minutes)
    total_seconds_step_1 = sum(seconds)
    minutes_to_add, total_seconds_final = figure_out_base_sixty(total_seconds_step_1)
    total_minutes_step2 = total_minutes_step_1 + minutes_to_add
    if total_minutes_step2 > 59 or hours:
        calculated_hours, total_minutes = figure_out_base_sixty(total_minutes_step2)
        final_hours = calculated_hours + total_hours_step_1
        return f"{final_hours}:{total_minutes:02d}:{total_seconds_final:02d}"
    else:
        total_minutes = total_minutes_step2
        return f"{total_minutes}:{total_seconds_final:02d}"
