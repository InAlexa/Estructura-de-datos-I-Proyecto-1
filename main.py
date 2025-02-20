from vehicle import Vehicle

def main():
    vehiculo = Vehicle("P444JDY", "Toyota", "Corolla", 2030, 50000, "blablabla")

    print("Placa:", vehiculo.get_plate())
    print("Marca:", vehiculo.get_brand())
    print("Modelo:", vehiculo.get_model())
    print("Año:", vehiculo.get_year())
    print("Kilometraje:", vehiculo.get_mileage())
    print("Historial:", vehiculo.get_record())


main()
