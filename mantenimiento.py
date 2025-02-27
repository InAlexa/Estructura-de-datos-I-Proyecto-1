from datetime import datetime
from nodo import Nodo

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.set_fecha(fecha)
        self.descripcion = descripcion
        self.set_costo(costo)

    def set_fecha(self, fecha):
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            self.fecha = fecha
        except ValueError:
            raise ValueError("Fecha inválida. Use el formato YYYY-MM-DD.")

    def set_costo(self, costo):
        if costo < 0:
            raise ValueError("El costo debe ser un número positivo.")
        self.costo = costo

    def __str__(self):
        return f"{self.fecha} - {self.descripcion}: Q.{self.costo}"

class ListaMantenimientos:
    def __init__(self):
        self.head = None

    def agregar_mantenimiento(self, mantenimiento):
        nuevo_nodo = Nodo(mantenimiento)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def mostrar_historial(self):
        actual = self.head
        if not actual:
            print("No hay mantenimientos registrados.")
            return
        while actual:
            print(actual.data)
            actual = actual.next

    def calcular_costo_total(self):
        total = 0
        actual = self.head
        while actual:
            total += actual.data.costo
            actual = actual.next
        return total
