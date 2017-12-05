class rpnCalculator:

    def __init__(self):
        self.values = list()

    def pushValue(self, value):
        self.values.append(value)

    def popValue(self):
        try:
            return self.values.pop()
        except IndexError:
            print('ERROR: No elements on stack.')

    def add(self):
        try:
            el1 = self.values.pop()
            el2 = self.values.pop()
        except IndexError:
            print('ERROR: Not enough elements on stack to perform a sum.')
        else:
            self.values.append(el1+el2)

    def sub(self):
        try:
            el1 = self.values.pop()
            el2 = self.values.pop()
        except IndexError:
            print('ERROR: Not enough elements on stack to perform a subtration.')
        else:
            self.values.append(el1-el2)
