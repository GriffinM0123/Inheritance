class Person:
    def __init__(self, pname, add, tnum):
        self.__pname = pname
        self.__add = add
        self.__tnum = tnum

    def print_person(self):
        print("The name of the person is: ", self.__pname)
        print("The address of the person is: ", self.__add)
        print("The number of the person is: ", self.__tnum)


class Customer(Person):
    def __init__(self, pname, add, tnum, cnum, Bool):

        Person.__init__(self, pname, add, tnum)

        self.__cnum = cnum
        self.__Bool = Bool

    def print_person(self):
        Person.print_person(self)
        print("The customer number is: ", self.__cnum)
        print("The mail preference of the customer is: ", self.__Bool)
