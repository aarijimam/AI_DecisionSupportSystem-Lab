import math

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def mag(self):
        return math.sqrt(self.real ** 2 + self.img ** 2)

    def orient(self):
        return math.atan(self.img / self.real)


if __name__ == '__main__':
    num1 = Complex(1,2)
    print(num1.mag())
    print(num1.orient())
   
