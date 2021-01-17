import math
from abc import ABC, abstractmethod


class Number(ABC):

    def __init__(self, num):
        self.real = num

    @abstractmethod
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __mul__(self, other):
        pass


class Real(Number):

    def __init__(self, num, rep):
        self.num = num
        self.representation = rep

    def __add__(self, num):
        if not isinstance(num, Real):
            raise Exception("Can't add {} with Real number".format(type(num)))

        if num.representation in ["pi", "e", "square root 3"]:
            self.num = self.num + num.num

    def __str__(self):
        return self.representation


class Complex(Number):

    def __init__(self, real, imaginary):
        super(self.__class__, self).__init__(real)
        self.imaginary = imaginary

    def __add__(self, num):
        super(self.__class__, self).__add__(num)
        if not isinstance(num, Complex):
            return "Input Error"

        self.real = self.real + num.real
        self.imaginary = self.imaginary + num.imaginary

    def __sub__(self, no):
        self.real = self.real - no.real
        self.imaginary = self.imaginary - no.imaginary

    def __mul__(self, no):
        real1 = self.real * no.real
        complex1 = self.real * no.complex
        complex2 = self.complex * no.real
        real2 = (-1) * self.complex * no.complex
        self.real = real1 + real2
        self.complex = complex1 + complex2

    def __truediv__(self, no):
        r1, i1 = self.real, self.imaginary
        r2, i2 = no.real, no.imaginary
        real_part = (r1*r2 + i1*i2) / (r2*r2 + i2*i2)
        imaginary_part = (i1*r2 - r1 * i2) / (r2*r2 + i2*i2)
        return Complex(real_part,imaginary_part)

    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    try:
        # Cr, Ci = [float(x) for x in input().split()]
        # Dr, Di = [float(x) for x in input().split()]
        Cr, Ci = [1.0, 2.0]
        Dr, Di = [2.0, 3.0]
        C = Complex(real=Cr, imaginary=Ci)
        D = Complex(real=Dr, imaginary=Di)
        C.__add__(D) # C = C  + D
        print(C.__str__())
        if isinstance(C, Number):
            print("C is a number")

        R1 = Real(math.pi, "pi")
        R2 = Real(math.pi, "pi")
        R1.__add__(num=R2)
        # R1.__add__(num=D) # R1 = R1 + D # Pi + (2 + 3i)

        lst = [C, D, R1, R2]
        for i in lst:
            i.__str__()

        # n = Number(num=1) not possible - abstract
    except Exception as e:
        raise e