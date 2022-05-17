# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length
#
#     def perimeter(self):
#         return 4 * self.length


# https: // realpython.com / python - super /
# https://www.programiz.com/python-programming/methods/built-in/super
"""With Super"""

class Rectangle1:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square1(Rectangle1):
    def __init__(self, length,width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle1):
    def  __init__(self, length, width, height):
        super().__init__(length, width)
        self.height= height

    def Volume(self):
        return  self.length * self.width * self.height

square=Square1(2,2)
cube = Cube(3, 3, 3)
print(square.area())
print(cube.Volume())