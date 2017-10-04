# coding=utf-8

class Edad:
    def evaluar_edad(self, edad):
        if not isinstance(edad, (int, float)):
            print('debes insertar un número')
        elif edad < 0:
            print('no existes')
        elif edad == 0:
            print('eres un recién nacido')
        elif edad < 13:
            print('eres niño')
        elif edad < 18:
            print('eres adolescente')
        elif edad < 65:
            print('eres adulto')
        elif edad < 120:
            print('eres adulto mayor')
        else:
            print('eres Mumm-Ra')
