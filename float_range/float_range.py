class float_range:
    def __init__(self, start=0, stop=0, increment=1):
        self.start = start
        self.stop = stop
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        next_number = self.start
        self.start += self.increment
        return next_number

    def __call__(self, *args, **kwargs):
        return 