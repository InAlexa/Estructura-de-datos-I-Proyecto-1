from flota import FlotaVehiculos

def main():
    flota = FlotaVehiculos()
    bandera = 0
    while bandera == 0:
        print("Menú")
        print("1. Registrar vehículo")
        print("2. Eliminar vehículo")
        print("3. Buscar vehículo")
        print("4. Listar vehículos")
        print("5. Agregar Mantenimiento")
        print("6. Ver Historial de Mantenimientos")
        print("7. Calcular Costo Total")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placa = input("Ingrese la placa: ")
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            anio = int(input("Ingrese el año: "))
            kilometraje = int(input("Ingrese el kilometraje: "))
            try:
                flota.registrar_vehiculo(placa, marca, modelo, anio, kilometraje)
                print("Vehículo registrado con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo que desea eliminar: ")
            flota.eliminar_vehiculo(placa)

        elif opcion == "3":
            placa = input("Ingrese la placa del vehículo que desea buscar: ")
            vehiculo = flota.buscar_vehiculo(placa)
            print(vehiculo if vehiculo else "Vehículo no encontrado.")

        elif opcion == "4":
            flota.listar_vehiculos()

        elif opcion == "5":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                fecha = input("Ingrese la fecha del mantenimiento (YYYY-MM-DD): ")
                descripcion = input("Ingrese la descripción: ")
                costo = float(input("Ingrese el costo: "))
                try:
                    vehiculo.agregar_mantenimiento(fecha, descripcion, costo)
                    print("Mantenimiento agregado con éxito.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "6":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                vehiculo.mostrar_historial()
            else:
                print("Vehículo no encontrado.")

        elif opcion == "7":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                total = vehiculo.calcular_costo_total()
                print(f"Costo total de mantenimientos: ${total}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "8":
            print("Saliendo...")
            bandera = 1
        else:
            print("Opción inválida.")

main()
