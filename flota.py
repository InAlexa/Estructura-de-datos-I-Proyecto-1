from nodo import Nodo
from vehiculo import Vehiculo

class FlotaVehiculos:
    def __init__(self):
        self.head = None
        self.tail = None

    def registrar_vehiculo(self, placa, marca, modelo, anio, kilometraje):
        nuevo_vehiculo = Vehiculo(placa, marca, modelo, anio, kilometraje)
        nuevo_nodo = Nodo(nuevo_vehiculo)

        if not self.head:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

    def eliminar_vehiculo(self, placa):
        actual = self.head
        while actual:
            if actual.data.placa == placa:
                if actual.prev:
                    actual.prev.next = actual.next
                if actual.next:
                    actual.next.prev = actual.prev
                if actual == self.head:
                    self.head = actual.next
                if actual == self.tail:
                    self.tail = actual.prev
                print(f"Vehículo {placa} eliminado con éxito.")
                return
            actual = actual.next
        print("Vehículo no encontrado.")

    def buscar_vehiculo(self, placa):
        actual = self.head
        while actual:
            if actual.data.placa == placa:
                return actual.data
            actual = actual.next
        return None

    def listar_vehiculos(self):
        actual = self.head
        if not actual:
            print("No hay vehículos registrados.")
            return
        while actual:
            print(actual.data)
            actual = actual.next
