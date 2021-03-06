class Complex:
 
    def __init__(self, x, y):
        self.rez = x
        self.im = y
 
    def __repr__(self):
        return f'Complex: {self.rez} + ({self.im})i'
 
    def __add__(self, right):
        if isinstance(right, int):
            return Complex(self.rez + right, self.im)
        if isinstance(right, Complex):
            return Complex(self.rez + right.rez, self.im + right.im)
 
    def __eq__(self, right):
        if isinstance(right, Complex):
            return (right.rez == self.rez) and (right.im == self.im)
 
    def __abs__(self):
        return (self.rez ** 2 + self.im ** 2) ** 0.5
 
 
a = Complex(1, -5)
b = Complex(1, -5)
print(a == b)
print(abs(a))