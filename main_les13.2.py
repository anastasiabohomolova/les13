
class A:
    def __init__(self, *atr):
        self.__atr = atr

class B(A):
    @property
    def method(self):
        return self.__atr

    @method.setter
    def method(self, *arg):
        new_el = input('print new el: ')
        arg = new_el
        self.__atr = arg


o = B()
o.method = 5, 566, 2323
print(o.method)
print(o.__dict__)


