# Golubovich Igor for Python Course | homework №6 | task №1

import math

class Compl:

    def __init__(self, c1, c2):
        self.c1 = complex(c1)
        self.c2 = complex(c2)

    def __repr__(self):
        return f'summ = {self.c1 + self.c2}\nsub = {self.c1 - self.c2}\nmul = {self.c1 * self.c2}\ndiv = {self.c1 / self.c2}\nmod_c1 = {abs(self.c1)}\nmod_c2 = {abs(self.c2)}'

        


p = Compl(1 + 2j, 2 + 4j)
print(p)
