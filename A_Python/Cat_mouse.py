#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

def catAndMouse(x, y, z):
    a = abs(x - z)
    b = abs(y - z)

    return "Cat A" if a < b else "Cat B" if b < a else "Mouse C"