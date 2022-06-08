
from  abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    # def mouse(self):
    #     pass
    def Keyboard(self):
        pass

    def Mouse(self):
        print("Here!! I am mouse")
class Laptop(Computer):
    def keypad(self):
        print("not need mouse")
    def Keyboard(self):
        # print("Its a need a Keyboard to operate")
        pass

lap=Laptop()
lap.Keyboard()