import math


def sum_timestamps(timestamps: list) -> str:
    """Accept a list of timestamps (in the format of MM:SS) and return a timestamp that is the sum of all given times.

    :param timestamps: A list of timestamps.
    :type timestamps: list
    :returns: Timestamp sum of all times in the list.
    """
    split_minutes_seconds = [timestamp.split(':') for timestamp in timestamps]
    minutes = []
    seconds = []
    for timestamp in split_minutes_seconds:
        minutes.append(int(timestamp[0]))
        seconds.append(int(timestamp[1]))
    total_minutes = sum(minutes)
    total_seconds_step_1 = sum(seconds)
    minutes_to_add = 0
    total_seconds_final = 0
    if total_seconds_step_1 > 59:
        minutes_to_add = math.floor(total_seconds_step_1/60)
        total_seconds_final = total_seconds_step_1 % 60
    else:
        total_seconds_final = total_seconds_step_1
    return f"{total_minutes+minutes_to_add}:{total_seconds_final:02d}"
