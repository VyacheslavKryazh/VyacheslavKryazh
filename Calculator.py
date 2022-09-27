
class Calculator:
    def __init__(self, x1, x2):# просто пустой инициализатор
        if x2 == 0:
            raise divizorEqualZero(x2)
        self.x1 = x1
        self.x2 = x2

    def add(self): # метод сложения двух переменных
        return self.x1 + self.x2

    def subtr(self):
        return self.x1 - self.x2

    def mult(self):
        return self.x1 * self.x2

    def div(self):
        return self.x1 / self.x2






