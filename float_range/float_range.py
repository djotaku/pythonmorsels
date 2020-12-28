class float_range:
    def __init__(self, *parameters):
        if len(parameters) == 3:
            self.start, self.stop, self.increment = parameters
        elif len(parameters) == 2:
            self.start, self.stop = parameters
            self.increment = 1.0
        elif len(parameters) == 1:
            self.stop = parameters[0]
            self.start = 0.0
            self.increment = 1.0
        else:
            raise TypeError

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

    def __call__(self, *parameters):
        if len(parameters) == 3:
            self.start, self.stop, self.increment = parameters
        elif len(parameters) == 2:
            self.start, self.stop = parameters
            self.increment = 1.0
        elif len(parameters) == 1:
            self.stop = parameters[0]
            self.start = 0.0
            self.increment = 1.0
        else:
            raise TypeError

    def __len__(self):
        pass

    def __reversed__(self):
        hold_start = self.start
        self.start = self.stop
        self.stop = hold_start
        self.increment = - self.increment


if __name__ == '__main__':
    for n in float_range(0.5, 2.5, 0.5):
        print(n)
    for n in float_range(2.5, 0, -0.5):
        print(n)
    for n in float_range(3.0):
        print(n)
    print(list(reversed(float_range(0.5, 2.5, 0.5))))
    r = float_range(0.5, 2.5, 0.5)
    print(list(r))
    print(list(r))
