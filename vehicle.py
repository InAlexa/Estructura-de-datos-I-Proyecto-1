from datetime import datetime
now = datetime.now().year # esto es para obtener el año actual

class Vehicle():
    def __init__(self, plate, brand, model, year, mileage, record):
        self.__plate =  plate
        self.__brand = brand
        self.__model = model
        self.set_year(year)
        self.__mileage = mileage
        self.__record = record # el __ para indicar que son atributos privados


    # getters y setters para poder modificar los atributos controlando la priv
    # car's plate
    def get_plate(self):
        return self.__plate
    def set_plate(self, plate):
        self.__plate = plate

    #car's brand
    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        self.__brand = brand

    #car's model
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model

    # car's year
    def get_year(self):
        return self.__year
    def set_year(self, year): #aqui voy a definir que el año del vehiculo sea coherente
        if year < 1900 or year > now:
            print("El año no es válido.")
            self.__year = "No se ha guardado nada"
        else:
            self.__year = year

    # car's mileage
    def get_mileage(self):
        return self.__mileage
    def set_mileage(self, mileage):
        if mileage < 0:
            print("El kilometraje no puede ser negativo.")
        else:
            self.__mileage = mileage

    # car's record
    def get_record(self):
        return self.__record
    def set_record(self, record):
        self.__record = record

