from datetime import datetime
from mantenimiento import ListaMantenimientos, Mantenimiento


class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.set_placa(placa)
        self.marca = marca
        self.modelo = modelo
        self.set_anio(anio)
        self.set_kilometraje(kilometraje)
        self.historial = ListaMantenimientos()

    def set_placa(self, placa):
        if len(placa) != 7 or not placa[:3].isalpha() or not placa[3:].isdigit():
            raise ValueError("Formato de placa inválido. Use tres letras seguidas de cuatro números (ej: ABC1234).")
        self.placa = placa.upper()

    def set_anio(self, anio):
        anio_actual = datetime.now().year
        if not (1900 <= anio <= anio_actual):
            raise ValueError("El año del vehículo debe estar entre 1900 y el año actual.")
        self.anio = anio

    def set_kilometraje(self, kilometraje):
        if kilometraje < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self.kilometraje = kilometraje

    def agregar_mantenimiento(self, fecha, descripcion, costo):
        mantenimiento = Mantenimiento(fecha, descripcion, costo)
        self.historial.agregar_mantenimiento(mantenimiento)

    def mostrar_historial(self):
        print(f"Historial de mantenimientos del vehículo {self.placa}:")
        self.historial.mostrar_historial()

    def calcular_costo_total(self):
        return self.historial.calcular_costo_total()

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo} ({self.anio}) - {self.kilometraje} km"
