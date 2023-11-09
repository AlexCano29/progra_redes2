'''
Autor: Julián Alexis Cano Cruces
Fecha 8/11/23
Ejercicio: Lab 3.2.1.15
'''

class QueueError(Exception):  # Eligir la clase base para la nueva excepción.
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.__queue:
            raise QueueError("La cola está vacía")
        return self.__queue.pop()


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")