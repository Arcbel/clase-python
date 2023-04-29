class Empleado():
    sueldo_base = 100.000

    def __init__(self, name): 
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod                   ## getter y setter de los atributos generales de las clases
    def get_sueldo_base(cls):      ## nombre arbitrario
        return cls.sueldo_base
    @classmethod
    def set_sueldo_base(cls, sueldo):
        cls.sueldo_base = sueldo