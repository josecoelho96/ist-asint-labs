try:
    infobj = open('data', 'r')
except IOError:
    print "That file does not exist"
else:
    v1 = infobj.readlines()
    for s in v1:
        print s