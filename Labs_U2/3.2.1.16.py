'''
Autor: Julián Alexis Cano Cruces
Fecha 8/11/23
Ejercicio: Lab 3.2.1.16
''' 

class QueueError(Exception):
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

    def isempty(self):
        return not bool(self.__queue)

class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")