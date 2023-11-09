'''
Autor: Julián Alexis Cano Cruces
Fecha 8/11/23
Ejercicio: Lab 3.2.1.14
'''

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__() 
        self.__counter = 0 # Llena el constructor con acciones apropiadas.
    

    def get_counter(self):
      return self.__counter
    

    def pop(self):
        val = super().pop() 
        self.__counter += 1 
        return val    # Haz un pop y actualiza el contador.

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())