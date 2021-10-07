# Golubovich Igor for Python Course | homework №6 | task №1

import math

class Compl:

    def __init__(self, c1, c2):
        self.c1 = complex(c1)
        self.c2 = complex(c2)

    def summ_c(self):
        return f'summ = {self.c1 + self.c2}'

    def sub_c(self):
        return f'sub = {self.c1 - self.c2}'

    def mul_c(self):
        return f'mul = {self.c1 * self.c2}'
    
    def div_c(self):
        return f'div = {self.c1 / self.c2}'

    def mod_c(self):
        a = abs(self.c1)
        b = abs(self.c2)
        return f'mod_c1 = {a}\nmod_c2 = {b}'

    # def __repr__(self):
    #     return f'summ = {self.c1 + self.c2}\nsub = {self.c1 - self.c2}\nmul = {self.c1 * self.c2}\ndiv = {self.c1 / self.c2}\nmod_c1 = {abs(self.c1)}\nmod_c2 = {abs(self.c2)}'

    # def __repr__(self):
    #     return self.summ_c()

        

p = Compl(1 + 2j, 2 + 4j)
print(p.summ_c())
print(p.sub_c())
print(p.mul_c())
print(p.div_c())
print(p.mod_c())
# print(p)