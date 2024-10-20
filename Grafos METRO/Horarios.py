from datetime import time
import metrodijkstra 

# Opciones semanales
opciones = {
    "1": "Lunes a viernes",
    "2": "Sábado",
    "3": "Domingo y festivos"
}

#Opcion semana
def elegir_opcion():
    # Mostrar las opciones disponibles
    print("Elige una opción:")
    for clave, valor in opciones.items():
        print(f"{clave}. {valor}")
    
    # Solicitar al usuario que elija una opción
    opcion = input("Ingresa el número de la opción que deseas elegir: ")
    
    # Verificar si la opción ingresada es válida
    if opcion in opciones:
        print(f"Has elegido: {opciones[opcion]}")
        return opciones[opcion]
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
        return None

# Definir los horarios para punta, valle y express
horarios = {
    #Lunes a Viernes
    "bajo_mañana": (time(6,0),time(6,59)),
    "punta_mañana": (time(7,0), time(8,59)),
    "valle_mañana": (time(9,0), time(17,59)),
    
    "punta_tarde": (time(18, 0), time(19,59)),
    "valle_tarde": (time(20,0), time(20,44)),
    "bajo_tarde": (time(20,45),time(23,0)),
    
    "express_mañana": (time(6,0), time(9,0)),
    "express_tarde": (time(18,0), time(21,0)),
    
    #Sabado
    "valle_Sabado": (time(6,30),time(23,0)),
    
    #Domingo y festivos
    "valle_DomingoFestivo": (time(8,0),time(23,0))
}

#Horario Lunes a Viernes

def verificar_horario_LunesViernes(hora_str):
    # Convertir la hora ingresada en formato HH:MM a un objeto de tipo time
    hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
    
    # Verificar en qué horario cae la hora ingresada
    if horarios["bajo_mañana"][0] <= hora_ingresada <= horarios["bajo_mañana"][1]:
        return "Horario bajo mañana " + verificar_horario_LunesViernes_express(hora_ingresada)
    elif horarios["bajo_tarde"][0] <= hora_ingresada <= horarios["bajo_tarde"][1]:
        return "Horario bajo tarde " + verificar_horario_LunesViernes_express(hora_ingresada)
    elif horarios["punta_mañana"][0] <= hora_ingresada <= horarios["punta_mañana"][1]:
        return "Horario Punta mañana " + verificar_horario_LunesViernes_express(hora_ingresada)
    elif horarios["punta_tarde"][0] <= hora_ingresada <= horarios["punta_tarde"][1]:
        return "Horario Punta tarde " + verificar_horario_LunesViernes_express(hora_ingresada)
    elif horarios["valle_mañana"][0] <= hora_ingresada <= horarios["valle_mañana"][1]:
        return "Horario Valle mañana " + verificar_horario_LunesViernes_express(hora_ingresada)
    elif horarios["valle_tarde"][0] <= hora_ingresada <= horarios["valle_tarde"][1]:
        return "Horario Valle tarde " + verificar_horario_LunesViernes_express(hora_ingresada)
    else:
        return "Fuera de horario de servicio"

# Verificar si es horario express
def verificar_horario_LunesViernes_express(hora):
    if horarios["express_mañana"][0] <= hora <= horarios["express_mañana"][1]:
        metrodijkstra.OrigenDestino_express(hora)
        return "y es Horario Express mañana"
    elif horarios["express_tarde"][0] <= hora <= horarios["express_tarde"][1]:
        metrodijkstra.OrigenDestino_express(hora)
        return "y es Horario Express tarde"
    else:
        metrodijkstra.OrigenDestino_baja(hora)
        return "y No es horario express"

#Horario Sabado
def verificar_horario_Sabado(hora_str):

    hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
    
    if horarios["valle_Sabado"][0] <= hora_ingresada <= horarios["valle_Sabado"][1]:
        metrodijkstra.OrigenDestino_baja(hora_ingresada)
        return "Horario Valle"
    else:
        return "Fuera de horario de servicio"
  
#Horario Domingo y festivos  
def verificar_horario_DomingoFestivo(hora_str):

    hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
    
    if horarios["valle_DomingoFestivo"][0] <= hora_ingresada <= horarios["valle_DomingoFestivo"][1]:
        metrodijkstra.OrigenDestino_baja(hora_ingresada)
        return "Horario Valle"
    else:
        return "Fuera de horario de servicio"
    
    
#####################################LLEGADA###########################
def verificar_horario_LunesViernes_llegada(hora_str):
    try:
        # Convertir la hora ingresada en formato HH:MM a un objeto de tipo time
        hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
        
        # Verificar en qué horario cae la hora ingresada
        if horarios["bajo_mañana"][0] <= hora_ingresada <= horarios["bajo_mañana"][1]:
            return "Horario bajo mañana " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        elif horarios["bajo_tarde"][0] <= hora_ingresada <= horarios["bajo_tarde"][1]:
            return "Horario bajo tarde " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        elif horarios["punta_mañana"][0] <= hora_ingresada <= horarios["punta_mañana"][1]:
            return "Horario Punta mañana " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        elif horarios["punta_tarde"][0] <= hora_ingresada <= horarios["punta_tarde"][1]:
            return "Horario Punta tarde " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        elif horarios["valle_mañana"][0] <= hora_ingresada <= horarios["valle_mañana"][1]:
            return "Horario Valle mañana " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        elif horarios["valle_tarde"][0] <= hora_ingresada <= horarios["valle_tarde"][1]:
            return "Horario Valle tarde " + verificar_horario_LunesViernes_express_llegada(hora_ingresada)
        else:
            return "Fuera de horario de servicio"
    
    except ValueError:
        return "Formato de hora incorrecto."

# Verificar si es horario express
def verificar_horario_LunesViernes_express_llegada(hora):
    # Verificar si es horario express
    if horarios["express_mañana"][0] <= hora <= horarios["express_mañana"][1]:
        metrodijkstra.OrigenDestino_express_llegada(hora)
        return "y es Horario Express mañana"
    elif horarios["express_tarde"][0] <= hora <= horarios["express_tarde"][1]:
        metrodijkstra.OrigenDestino_express_llegada(hora)
        return "y es Horario Express tarde"
    else:
        metrodijkstra.OrigenDestino_baja(hora)
        return "y No es horario express"

#Horario Sabado
def verificar_horario_Sabado_llegada(hora_str):
    try:
        hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
        
        if horarios["valle_Sabado"][0] <= hora_ingresada <= horarios["valle_Sabado"][1]:
            metrodijkstra.OrigenDestino_baja_llegada(hora_ingresada)
            return "Horario Valle"
        else:
            return "Fuera de horario de servicio"
    
    except ValueError:
        return "Formato de hora incorrecto."
  
#Horario Domingo y festivos  
def verificar_horario_DomingoFestivo_llegada(hora_str):
    try:
        hora_ingresada = time(int(hora_str.split(':')[0]), int(hora_str.split(':')[1]))
        
        if horarios["valle_DomingoFestivo"][0] <= hora_ingresada <= horarios["valle_DomingoFestivo"][1]:
            metrodijkstra.OrigenDestino_baja_llegada(hora_ingresada)
            return "Horario Valle"
        else:
            return "Fuera de horario de servicio"
    
    except ValueError:
        return "Formato de hora incorrecto."