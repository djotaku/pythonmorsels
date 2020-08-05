import collections
import collections.abc


def tail(sequence, number_of_elements):
    if number_of_elements > 0:
        if isinstance(sequence, collections.abc.Sequence):
            return list(sequence[-number_of_elements:])
        else:
            deque = collections.deque(maxlen=number_of_elements)
            for item in sequence:
                deque.append(item)
            return list(deque)
    else:
        return []