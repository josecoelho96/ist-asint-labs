from rpnCalculator import rpnCalculator

calc1 = rpnCalculator()

calc1.pushValue(5)
calc1.pushValue(6)

calc1.add()

print(calc1.popValue())