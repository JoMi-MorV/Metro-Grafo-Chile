import Horarios
import metrodijkstra
from datetime import time
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

def actual():
    
    now = datetime.now()
    now = now.strftime("%H:%M")
    horario_elegido = Horarios.elegir_opcion()
    print(f"La hora actual es: {now}")
    
    if horario_elegido == 'Lunes a viernes':
        resultado = Horarios.verificar_horario_LunesViernes(now)
        print(resultado)

    if horario_elegido == 'Sábado':
            resultado = Horarios.verificar_horario_Sabado(now)
            print(resultado)

    if horario_elegido == 'Domingo y festivos':
        
        resultado = Horarios.verificar_horario_DomingoFestivo(now)
        print(resultado)
    
def llegada():
    
    hora = input("Ingrese la hora de llegada (HH:MM): ")
    try:
        print(f"Hora de llegada programada: {hora}")
    except ValueError:
        print("Error: Formato de hora incorrecto. Asegúrese de usar HH:MM.")
        
    opcion_elegida = Horarios.elegir_opcion()
    
    # Ejecutar la función para verificar el horario de Lunes a Viernes
    if opcion_elegida == 'Lunes a viernes':
        
        resultado = Horarios.verificar_horario_LunesViernes_llegada(hora)
        print(resultado)

    # Ejecutar la función para verificar el horario del Sábado
    if opcion_elegida == 'Sábado':
        resultado = Horarios.verificar_horario_Sabado_llegada(hora)
        print(resultado)

    # Ejecutar la función para verificar el horario de Domingo y festivos
    if opcion_elegida == 'Domingo y festivos':
        resultado = Horarios.verificar_horario_DomingoFestivo_llegada(hora)
        print(resultado)  
    
    
    
    
    
def salida():

    hora = input("Ingresa una hora en formato HH:MM: ")
    try:
        print(f"Hora de salida programada: {hora}")
    except ValueError:
        print("Error: Formato de hora incorrecto. Asegúrese de usar HH:MM.")

    opcion_elegida = Horarios.elegir_opcion()

    # Ejecutar la función para verificar el horario de Lunes a Viernes
    if opcion_elegida == 'Lunes a viernes':
        
        resultado = Horarios.verificar_horario_LunesViernes(hora)
        print(resultado)

    # Ejecutar la función para verificar el horario del Sábado
    if opcion_elegida == 'Sábado':
        resultado = Horarios.verificar_horario_Sabado(hora)
        print(resultado)

    # Ejecutar la función para verificar el horario de Domingo y festivos
    if opcion_elegida == 'Domingo y festivos':
        resultado = Horarios.verificar_horario_DomingoFestivo(hora)
        print(resultado)