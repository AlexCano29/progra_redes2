'''
Autor: Julián Alexis Cano Cruces
Fecha 8/11/23
Ejercicio: Lab 3.4.1.13
'''


class WeekDayError(Exception):
    pass

class Weeker:
    DAYS_OF_WEEK = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Día de la semana no válido")
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = self.DAYS_OF_WEEK[new_index]

    def subtract_days(self, n):
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = self.DAYS_OF_WEEK[new_index]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Invalido')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
