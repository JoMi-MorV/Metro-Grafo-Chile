from datetime import datetime
import metro_horario

def hora_actual():
    metro_horario.actual()

def ingresar_hora_llegada():
    metro_horario.llegada()

def ingresar_hora_salida():
    metro_horario.salida()

def main_menu():
    """Función principal para mostrar el menú."""
    while True:
        print("\nMenú:")
        print("1. Ver hora actual")
        print("2. Ingresar hora de llegada")
        print("3. Ingresar hora de salida")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            hora_actual()
        elif opcion == '2':
            ingresar_hora_llegada()
        elif opcion == '3':
            ingresar_hora_salida()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    main_menu()
