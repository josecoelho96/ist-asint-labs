print 'Please insert 20 numbers to calculate their average'

sum = 0
for x in range(20):
    a = float(raw_input("> "))
    if a < 0:
        break
    sum = sum + a
else:
    avg = sum/20
    print 'the average is %f' % avg