def addition(a, b):
    return a + b


var1 = addition(10, 26)
print(var1)


class Person:
    def __init__(self, person_name: str, phoneNumber: int, date_of_birth: str):
        self.__name = person_name
        self.__phone_number = phoneNumber
        self.__date_of_birth = date_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self.__hasAnyvalue(new_name):
            print("Name Cant have Value")
            return
        self.__name = new_name

    def __hasAnyvalue(self, string):
        return "0" in string

    def get_summery(self):
        return f"Name:{self.__name}, PhoneNumber:{self.__phone_number}, Date of Birth: {self.__date_of_birth}"

    def __str__(self):            #Also __repr__ can used in same way
        # return f"Name:{self.__name}, PhoneNumber:{self.__phone_number}, Date of Birth: {self.__date_of_birth}"
        return self.get_summery()


a_person = Person("Gaju", 1782057366, "18 july 1995")
print(a_person)
a_person.set_name("Gaju Ahmed")
# print(a_person.get_summery())
print(a_person)
a_person.set_name("0Gaju")
print(a_person.get_name())


