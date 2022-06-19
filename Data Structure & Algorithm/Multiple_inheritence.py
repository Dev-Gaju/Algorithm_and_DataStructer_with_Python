class first():
    def __init__(self):
        print("First")


class Second(first):
    def __init__(self):
        # super(Second, self).__init__()  sued super to access the parameter from parent class
        print("Second")


class Third(first):
    def method3(self):
        print("Third printed")


class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print("That's it")


a = Fourth()
a.method3()
# print("a looks like as ", a)

b = Third()
# print("b looks like as ", b)

c = Second()
