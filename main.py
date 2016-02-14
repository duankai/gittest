import os

def long_fun1_name(
        name,
        age):
    if (name == "kkk"
            and age > 12):
        print(name, age)
    print(name, age)

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

class Car(object):


    def __init__(self, arg):
        #super(, self).__init__()
        self.arg = arg

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def judge(self):
        if self.arg == "new Car":
            print("Ok")
        else:
            print("Refused")

if '__name__==__main__':

    long_fun1_name("kkk", 23)
    dic = {}
    dic['first'] = my_list[1]
    print(dic['first'])

    c = Car("new Car")
    c.start()
    c.stop()
    c.judge()
