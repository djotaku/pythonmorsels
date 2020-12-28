class float_range:
    def __init__(self, start=0.0, stop=0.0, increment=1.0):
        self.start = start
        self.stop = stop
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        next_number = self.start
        if self.increment > 0:
            if self.start < self.stop:
                self.start += self.increment
                return next_number
            else:
                raise StopIteration
        else:
            if self.start > self.stop:
                self.start += self.increment
                return next_number
            else:
                raise StopIteration

    def __call__(self, start=0.0, stop=0.0, increment=1.0):
        self.start = start
        self.stop = stop
        self.increment = increment


if __name__ == '__main__':
    for n in float_range(0.5, 2.5, 0.5):
        print(n)
    for n in float_range(2.5, 0, -0.5):
        print(n)
