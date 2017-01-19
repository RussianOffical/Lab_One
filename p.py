while True:
    a = input("ADDITION = 1 or SUBTRACTION = 2")
    if a == 1:
        print "ADDITION"
        x = input("First value")
        y = input("Second value")
        if type(x) == type(y):
            print type(x)
            print x + y
        else:
            print "Addition is unspecified for the input types given"
            print "*HINT* Try using the same type"
    if a == 2:
        print "SUBTRACTION"
        x = input("First value")
        y = input("Second value")
        if type(x) == type(y):
            print type(x)
            print x - y
        else:
            print "Addition is unspecified for the input types given"
            print "*HINT* Try using the same type"

