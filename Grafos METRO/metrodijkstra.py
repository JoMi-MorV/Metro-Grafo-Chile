import networkx as nx
import matplotlib.pyplot as plt


#Lineas de metro

#Linea 1
Linea_1 ={
    "San Pablo L1",
    "Neptuno",
    "Pajaritos",
    "Las Rejas",
    "Ecuador",
    "San Alberto Hurtado",
    "Universidad de Santiago",
    "Estación Central",
    "U.L.A",
    "República",
    "Los Héroes L1",
    "La Moneda",
    "Universidad de Chile L1",
    "Santa Lucía",
    "Universidad Católica",
    "Baquedano L1",
    "Salvador",
    "Manuel Montt",
    "Pedro de Valdivia",
    "Los Leones L1",
    "Tobalaba L1",
    "El Golf",
    "Alcántara",
    "Escuela Militar",
    "Manquehue",
    "Hernando de Magallanes",
    "Los Dominicos"
}

#Linea 2
linea_2 ={
    "Vespucio Norte",
    "Zapadores",
    "Dorsal",
    "Einstein",
    "Cementerios",
    "Cerro Blanco",
    "Patronato",
    "Puente Cal y Canto L2",
    "Santa Ana L2",
    "Los Héroes L2",
    "Toesca",
    "Parque O'Higgins",
    "Rondizzoni",
    "Franklin L2",
    "El Llano",
    "San Miguel",
    "Lo Vial",
    "Departamental",
    "Ciudad del Niño",
    "Lo Ovalle",
    "El Parrón",
    "La Cisterna L2",
    "El Bosque",
    "Observatorio",
    "Copa Lo Martinez",
    "Hospital El Pino"
}

#Linea 3
linea_3 = {
    "Plaza Quilicura",
    "Lo Cruzat",
    "Ferrocarril",
    "Los Libertadores",
    "Cardenal Caro",
    "Vivaceta",
    "Conchalí",
    "Plaza Chacabuco",
    "Hospitales",
    "Puente Cal y Canto L3",
    "Plaza de Armas L3",
    "Universidad de Chile L3",
    "Parque Almagro",
    "Matta",
    "Irarrázaval L3",
    "Monseñor Eyzaguirre",
    "Ñuñoa L3",
    "Chile España",
    "Villa Frei",
    "Plaza Egaña L3",
    "Fernando Castillo Velasco"
}

#Linea 4
linea_4 = {
    "Tobalaba L4",
    "Cristóbal Colón",
    "Francisco Bilbao",
    "Príncipe de Gales",
    "Simón Bolivar",
    "Plaza Egaña L4",
    "Los Orientales",
    "Grecia",
    "Los Presidentes",
    "Quilín",
    "Las Torres",
    "Macul",
    "Vicuña Mackenna L4",
    "Vicente Valdés L4",
    "Rojas Magallanes",
    "Trinidad",
    "San José de la Estrella",
    "Los Quillayes",
    "Elisa Correa",
    "Hospital Sótero del Río",
    "Protectora de la Infancia",
    "Las Mercedes",
    "Plaza de Puente Alto"
}

#Linea 4A
linea_4A = {
    "Vicuña Mackenna L4A",
    "Santa Julia",
    "La Granja",
    "Santa Rosa",
    "San Ramón",
    "La Cisterna L4A"
}

#Linea 5
linea_5 = {
    "Plaza de Maipú" ,
    "Santiago Bueras",
    "Del Sol",
    "Monte Tabor",
    "Las Parcelas",
    "Laguna Sur",
    "Barrancas",
    "Pudahuel",
    "San Pablo L5",
    "Lo Prado",
    "Blanqueado",
    "Gruta de Lourdes",
    "Quinta Normal",
    "Cumming",
    "Santa Ana L5",
    "Plaza de Armas L5",
    "Bellas Artes",
    "Baquedano L5",
    "Parque Bustamante",
    "Santa Isabel",
    "Irarrázaval L5",
    "Ñuble L5",
    "Rodrigo de Araya",
    "Carlos Valdovinos",
    "Camino Agrícola",
    "San Joaquín",
    "Pedrero",
    "Mirador",
    "Bellavista de La Florida",
    "Vicente Valdés L5"
}
#Linea 6
linea_6 = {
    "Cerrillos",
    "Lo Valledor",
    "Pdte. Pedro Aguirre Cerda",
    "Franklin L6",
    "Bío Bío",
    "Ñuble L6",
    "Estadio Nacional",
    "Ñuñoa L6",
    "Inés de Suárez",
    "Los Leones L6"
}

# Definir las estaciones de cada línea como un diccionario
estaciones_lineas = {
    "San Pablo L1": {"linea": "L1"},
    "Neptuno": {"linea": "L1"},
    "Pajaritos": {"linea": "L1"},
    "Las Rejas": {"linea": "L1"},
    "Ecuador": {"linea": "L1"},
    "San Alberto Hurtado": {"linea": "L1"},
    "Universidad de Santiago": {"linea": "L1"},
    "Estación Central": {"linea": "L1"},
    "U.L.A": {"linea": "L1"},
    "República": {"linea": "L1"},
    "Los Héroes L1": {"linea": "L1"},
    "La Moneda": {"linea": "L1"},
    "Universidad de Chile L1": {"linea": "L1"},
    "Santa Lucía": {"linea": "L1"},
    "Universidad Católica": {"linea": "L1"},
    "Baquedano L1": {"linea": "L1"},
    "Salvador": {"linea": "L1"},
    "Manuel Montt": {"linea": "L1"},
    "Pedro de Valdivia": {"linea": "L1"},
    "Los Leones L1": {"linea": "L1"},
    "Tobalaba L1": {"linea": "L1"},
    "El Golf": {"linea": "L1"},
    "Alcántara": {"linea": "L1"},
    "Escuela Militar": {"linea": "L1"},
    "Manquehue": {"linea": "L1"},
    "Hernando de Magallanes": {"linea": "L1"},
    "Los Dominicos": {"linea": "L1"},

    # Línea 2
    "Vespucio Norte": {"linea": "L2", "luz": ["rojo","verde"]},
    "Zapadores": {"linea": "L2", "luz": ["rojo","verde"]},
    "Dorsal": {"linea": "L2", "luz": ["rojo"]},
    "Einstein": {"linea": "L2", "luz": ["verde"]},
    "Cementerios": {"linea": "L2", "luz": ["rojo"]},
    "Cerro Blanco": {"linea": "L2", "luz": ["verde"]},
    "Patronato": {"linea": "L2", "luz": ["rojo"]},
    "Puente Cal y Canto L2": {"linea": "L2", "luz": ["rojo","verde"]},
    "Santa Ana L2": {"linea": "L2", "luz": ["rojo","verde"]},
    "Los Héroes L2": {"linea": "L2", "luz": ["rojo","verde"]},
    "Toesca": {"linea": "L2", "luz": ["verde"]},
    "Parque O'Higgins": {"linea": "L2", "luz": ["rojo"]},
    "Rondizzoni": {"linea": "L2", "luz": ["verde"]},
    "Franklin L2": {"linea": "L2", "luz": ["rojo","verde"]},
    "El Llano": {"linea": "L2", "luz": ["rojo"]},
    "San Miguel": {"linea": "L2", "luz": ["verde"]},
    "Lo Vial": {"linea": "L2", "luz": ["rojo"]},
    "Departamental": {"linea": "L2", "luz": ["verde"]},
    "Ciudad del Niño": {"linea": "L2", "luz": ["rojo"]},
    "Lo Ovalle": {"linea": "L2", "luz": ["rojo","verde"]},
    "El Parrón": {"linea": "L2", "luz": ["verde"]},
    "La Cisterna L2": {"linea": "L2", "luz": ["rojo","verde"]},
    "El Bosque": {"linea": "L2", "luz": ["rojo"]},
    "Observatorio": {"linea": "L2", "luz": ["verde"]},
    "Copa Lo Martinez": {"linea": "L2", "luz": ["rojo"]},
    "Hospital El Pino": {"linea": "L2", "luz": ["rojo","verde"]},

    # Línea 3
    "Plaza Quilicura": {"linea": "L3"},
    "Lo Cruzat": {"linea": "L3"},
    "Ferrocarril": {"linea": "L3"},
    "Los Libertadores": {"linea": "L3"},
    "Cardenal Caro": {"linea": "L3"},
    "Vivaceta": {"linea": "L3"},
    "Conchalí": {"linea": "L3"},
    "Plaza Chacabuco": {"linea": "L3"},
    "Hospitales": {"linea": "L3"},
    "Puente Cal y Canto L3": {"linea": "L3"},
    "Plaza de Armas L3": {"linea": "L3"},
    "Universidad de Chile L3": {"linea": "L3"},
    "Parque Almagro": {"linea": "L3"},
    "Matta": {"linea": "L3"},
    "Irarrázaval L3": {"linea": "L3"},
    "Monseñor Eyzaguirre": {"linea": "L3"},
    "Ñuñoa L3": {"linea": "L3"},
    "Chile España": {"linea": "L3"},
    "Villa Frei": {"linea": "L3"},
    "Plaza Egaña L3": {"linea": "L3"},
    "Fernando Castillo Velasco": {"linea": "L3"},

    # Línea 4
    "Tobalaba L4": {"linea": "L4", "luz": ["rojo","verde"]},
    "Cristóbal Colón": {"linea": "L4", "luz": ["verde"]},
    "Francisco Bilbao": {"linea": "L4", "luz": ["rojo","verde"]},
    "Príncipe de Gales": {"linea": "L4", "luz": ["rojo"]},
    "Simón Bolivar": {"linea": "L4", "luz": ["verde"]},
    "Plaza Egaña L4": {"linea": "L4", "luz": ["rojo","verde"]},
    "Los Orientales": {"linea": "L4", "luz": ["rojo"]},
    "Grecia": {"linea": "L4", "luz": ["verde"]},
    "Los Presidentes": {"linea": "L4", "luz": ["rojo"]},
    "Quilín": {"linea": "L4", "luz": ["verde"]},
    "Las Torres": {"linea": "L4", "luz": ["rojo"]},
    "Macul": {"linea": "L4", "luz": ["rojo","verde"]},
    "Vicuña Mackenna L4": {"linea": "L4", "luz": ["rojo","verde"]},
    "Vicente Valdés L4": {"linea": "L4", "luz": ["rojo","verde"]},
    "Rojas Magallanes": {"linea": "L4", "luz": ["verde"]},
    "Trinidad": {"linea": "L4", "luz": ["rojo"]},
    "San José de la Estrella": {"linea": "L4", "luz": ["verde"]},
    "Los Quillayes": {"linea": "L4", "luz": ["rojo"]},
    "Elisa Correa": {"linea": "L4", "luz": ["rojo","verde"]},
    "Hospital Sótero del Río": {"linea": "L4", "luz": ["rojo","verde"]},
    "Protectora de la Infancia": {"linea": "L4", "luz": ["verde"]},
    "Las Mercedes": {"linea": "L4", "luz": ["rojo"]},
    "Plaza de Puente Alto": {"linea": "L4", "luz": ["rojo","verde"]},

    # Línea 4A
    "Vicuña Mackenna L4A": {"linea": "L4A"},
    "Santa Julia": {"linea": "L4A"},
    "La Granja": {"linea": "L4A"},
    "Santa Rosa": {"linea": "L4A"},
    "San Ramón": {"linea": "L4A"},
    "La Cisterna L4A": {"linea": "L4A"},

    # Línea 5
    "Plaza de Maipú": {"linea": "L5", "luz": ["rojo","verde"]},
    "Santiago Bueras": {"linea": "L5", "luz": ["rojo"]},
    "Del Sol": {"linea": "L5", "luz": ["verde"]},
    "Monte Tabor": {"linea": "L5", "luz": ["rojo"]},
    "Las Parcelas": {"linea": "L5", "luz": ["verde"]},
    "Laguna Sur": {"linea": "L5", "luz": ["rojo","verde"]},
    "Barrancas": {"linea": "L5", "luz": ["rojo"]},
    "Pudahuel": {"linea": "L5", "luz": ["rojo","verde"]},
    "San Pablo L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Lo Prado": {"linea": "L5", "luz": ["verde"]},
    "Blanqueado": {"linea": "L5", "luz": ["rojo"]},
    "Gruta de Lourdes": {"linea": "L5", "luz": ["verde"]},
    "Quinta Normal": {"linea": "L5", "luz": ["rojo"]},
    "Cumming": {"linea": "L5", "luz": ["verde"]},
    "Santa Ana L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Plaza de Armas L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Bellas Artes": {"linea": "L5", "luz": ["rojo","verde"]},
    "Baquedano L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Parque Bustamante": {"linea": "L5", "luz": ["rojo"]},
    "Santa Isabel": {"linea": "L5", "luz": ["verde"]},
    "Irarrázaval L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Ñuble L5": {"linea": "L5", "luz": ["rojo","verde"]},
    "Rodrigo de Araya": {"linea": "L5", "luz": ["rojo"]},
    "Carlos Valdovinos": {"linea": "L5", "luz": ["verde"]},
    "Camino Agrícola": {"linea": "L5", "luz": ["rojo"]},
    "San Joaquín": {"linea": "L5", "luz": ["rojo","verde"]},
    "Pedrero": {"linea": "L5", "luz": ["verde"]},
    "Mirador": {"linea": "L5", "luz": ["rojo"]},
    "Bellavista de La Florida": {"linea": "L5", "luz": ["rojo","verde"]},
    "Vicente Valdés L5": {"linea": "L5", "luz": ["rojo","verde"]},

    # Línea 6
    "Cerrillos": {"linea": "L6"},
    "Lo Valledor": {"linea": "L6"},
    "Pdte. Pedro Aguirre Cerda": {"linea": "L6"},
    "Franklin L6": {"linea": "L6"},
    "Bío Bío": {"linea": "L6"},
    "Ñuble L6": {"linea": "L6"},
    "Estadio Nacional": {"linea": "L6"},
    "Ñuñoa L6": {"linea": "L6"},
    "Inés de Suárez": {"linea": "L6"},
    "Los Leones L6": {"linea": "L6"}
}

#definimos el metro y sus pesos(tiempo) entre estaciones

metro_opcion1 = {
    # Línea 1
    "San Pablo L1": {"Neptuno": 2,"San Pablo L5": 5},
    "Neptuno": {"San Pablo L1": 2, "Pajaritos": 2},
    "Pajaritos": {"Neptuno": 2, "Las Rejas": 2},
    "Las Rejas": {"Pajaritos": 2, "Ecuador": 2},
    "Ecuador": {"Las Rejas": 2, "San Alberto Hurtado": 2},
    "San Alberto Hurtado": {"Ecuador": 2, "Universidad de Santiago": 2},
    "Universidad de Santiago": {"San Alberto Hurtado": 2, "Estación Central": 2},
    "Estación Central": {"Universidad de Santiago": 2, "U.L.A": 2},
    "U.L.A": {"Estación Central": 2, "República": 2},
    "República": {"U.L.A": 2, "Los Héroes L1": 2},
    "Los Héroes L1": {"República": 2, "La Moneda": 2, "Los Héroes L2": 5},
    "La Moneda": {"Los Héroes L1": 2, "Universidad de Chile L1": 2},
    "Universidad de Chile L1": {"La Moneda": 2, "Santa Lucía": 2, "Universidad de Chile L3": 5},
    "Santa Lucía": {"Universidad de Chile L1": 2, "Universidad Católica": 2},
    "Universidad Católica": {"Santa Lucía": 2, "Baquedano L1": 2},
    "Baquedano L1": {"Universidad Católica": 2, "Salvador": 2, "Baquedano L5": 5},
    "Salvador": {"Baquedano L1": 2, "Manuel Montt": 2},
    "Manuel Montt": {"Salvador": 2, "Pedro de Valdivia": 2},
    "Pedro de Valdivia": {"Manuel Montt": 2, "Los Leones L1": 2},
    "Los Leones L1": {"Pedro de Valdivia": 2, "Tobalaba L1": 2, "Los Leones L6": 5},
    "Tobalaba L1": {"Los Leones L1": 2, "El Golf": 2, "Tobalaba L4": 5},
    "El Golf": {"Tobalaba L1": 2, "Alcántara": 2},
    "Alcántara": {"El Golf": 2, "Escuela Militar": 2},
    "Escuela Militar": {"Alcántara": 2, "Manquehue": 2},
    "Manquehue": {"Escuela Militar": 2, "Hernando de Magallanes": 2},
    "Hernando de Magallanes": {"Manquehue": 2, "Los Dominicos": 3},
    "Los Dominicos": {"Hernando de Magallanes": 3},

    # Línea 2
    "Vespucio Norte": {"Zapadores": 2},
    "Zapadores": {"Vespucio Norte": 2, "Dorsal": 2},
    "Dorsal": {"Zapadores": 2, "Einstein": 2},
    "Einstein": {"Dorsal": 2, "Cementerios": 2},
    "Cementerios": {"Einstein": 2, "Cerro Blanco": 2},
    "Cerro Blanco": {"Cementerios": 2, "Patronato": 2},
    "Patronato": {"Cerro Blanco": 2, "Puente Cal y Canto L2": 2},
    "Puente Cal y Canto L2": {"Patronato": 2, "Santa Ana L2": 3, "Puente Cal y Canto L3": 5},
    "Santa Ana L2": {"Puente Cal y Canto L2": 3, "Los Héroes L2": 2, "Santa Ana L5": 5},
    "Los Héroes L2": {"Santa Ana L2": 2, "Toesca": 2, "Los Héroes L1": 5},
    "Toesca": {"Los Héroes L2": 2, "Parque O'Higgins": 2},
    "Parque O'Higgins": {"Toesca": 2, "Rondizzoni": 2},
    "Rondizzoni": {"Parque O'Higgins": 2, "Franklin L2": 2},
    "Franklin L2": {"Rondizzoni": 2, "El Llano": 2, "Franklin L6": 5},
    "El Llano": {"Franklin L2": 2, "San Miguel": 2},
    "San Miguel": {"El Llano": 2, "Lo Vial": 2},
    "Lo Vial": {"San Miguel": 2, "Departamental": 2},
    "Departamental": {"Lo Vial": 2, "Ciudad del Niño": 2},
    "Ciudad del Niño": {"Departamental": 2, "Lo Ovalle": 2},
    "Lo Ovalle": {"Ciudad del Niño": 2, "El Parrón": 2},
    "El Parrón": {"Lo Ovalle": 2, "La Cisterna L2": 3},
    "La Cisterna L2": {"El Parrón": 3,"El Bosque": 2,"La Cisterna L4A": 5},
    "El Bosque": {"La Cisterna L2": 2, "Observatorio": 3},
    "Observatorio": {"El Bosque": 3, "Copa Lo Martinez": 2},
    "Copa Lo Martinez": {"Observatorio": 2, "Hospital El Pino": 3},
    "Hospital El Pino": {"Copa Lo Martinez": 3},

    # Línea 3
    "Plaza Quilicura": {"Lo Cruzat": 2},
    "Lo Cruzat": {"Plaza Quilicura": 2, "Ferrocarril": 3},
    "Ferrocarril": {"Lo Cruzat": 3, "Los Libertadores": 3},
    "Los Libertadores": {"Ferrocarril": 3, "Cardenal Caro": 2},
    "Cardenal Caro": {"Los Libertadores": 2, "Vivaceta": 3},
    "Vivaceta": {"Cardenal Caro": 3, "Conchalí": 3},
    "Conchalí": {"Vivaceta": 3, "Plaza Chacabuco": 3},
    "Plaza Chacabuco": {"Conchalí": 3, "Hospitales": 3},
    "Hospitales": {"Plaza Chacabuco": 3, "Puente Cal y Canto L3": 3},
    "Puente Cal y Canto L3": {"Hospitales": 3, "Plaza de Armas L3": 2, "Puente Cal y Canto L2": 5},
    "Plaza de Armas L3": {"Puente Cal y Canto L3": 2, "Universidad de Chile L3": 2, "Plaza de Armas L5": 5},
    "Universidad de Chile L3": {"Plaza de Armas L3": 2, "Parque Almagro": 2, "Universidad de Chile L1": 5},
    "Parque Almagro": {"Universidad de Chile L3": 2, "Matta": 3},
    "Matta": {"Parque Almagro": 3, "Irarrázaval L3": 3},
    "Irarrázaval L3": {"Matta": 3, "Monseñor Eyzaguirre": 3, "Irarrázaval L5": 5},
    "Monseñor Eyzaguirre": {"Irarrázaval L3": 3, "Ñuñoa L3": 2},
    "Ñuñoa L3": {"Monseñor Eyzaguirre": 2, "Chile España": 2, "Ñuñoa L6": 5},
    "Chile España": {"Ñuñoa L3": 2, "Villa Frei": 3},
    "Villa Frei": {"Chile España": 3, "Plaza Egaña L3": 2},
    "Plaza Egaña L3": {"Villa Frei": 2, "Fernando Castillo Velasco": 3, "Plaza Egaña L4": 5},
    "Fernando Castillo Velasco": {"Plaza Egaña L3": 3},

    # Línea 4
    "Tobalaba L4": {"Tobalaba L1": 5, "Cristóbal Colón": 2},
    "Cristóbal Colón": {"Tobalaba L4": 2, "Francisco Bilbao": 2},
    "Francisco Bilbao": {"Cristóbal Colón": 2, "Príncipe de Gales": 3},
    "Príncipe de Gales": {"Francisco Bilbao": 3, "Simón Bolívar": 2},
    "Simón Bolívar": {"Príncipe de Gales": 2, "Plaza Egaña L4": 2},
    "Plaza Egaña L4": {"Simón Bolívar": 2, "Los Orientales": 2, "Plaza Egaña L3": 5},
    "Los Orientales": {"Plaza Egaña L4": 2, "Grecia": 2},
    "Grecia": {"Los Orientales": 2, "Los Presidentes": 2},
    "Los Presidentes": {"Grecia": 2, "Quilín": 2},
    "Quilín": {"Los Presidentes": 2, "Las Torres": 2},
    "Las Torres": {"Quilín": 2, "Macul": 2},
    "Macul": {"Las Torres": 2, "Vicuña Mackenna L4": 3},
    "Vicuña Mackenna L4": {"Macul": 3, "Vicente Valdés L4": 2, "Vicuña Mackenna L5": 5},
    "Vicente Valdés L4": {"Vicuña Mackenna L4": 2, "Rojas Magallanes": 2, "Vicente Valdés L5": 5},
    "Rojas Magallanes": {"Vicente Valdés L4": 2, "Trinidad": 2},
    "Trinidad": {"Rojas Magallanes": 2, "San José de la Estrella": 2},
    "San José de la Estrella": {"Trinidad": 2, "Los Quillayes": 2},
    "Los Quillayes": {"San José de la Estrella": 2, "Elisa Correa": 2},
    "Elisa Correa": {"Los Quillayes": 2, "Hospital Sótero del Río": 2},
    "Hospital Sótero del Río": {"Elisa Correa": 2, "Protectora de la Infancia": 2},
    "Protectora de la Infancia": {"Hospital Sótero del Río": 2, "Las Mercedes": 2},
    "Las Mercedes": {"Protectora de la Infancia": 2, "Plaza de Puente Alto": 3},
    "Plaza de Puente Alto": {"Las Mercedes": 3},

    # Línea 4A
    "La Cisterna L4A": {"La Cisterna L2": 5, "San Ramón": 5},
    "San Ramón": {"La Cisterna L4A": 5, "Santa Rosa": 2},
    "Santa Rosa": {"San Ramón": 2, "La Granja": 4},
    "La Granja": {"Santa Rosa": 4, "Santa Julia": 2},
    "Santa Julia": {"La Granja": 2, "Vicuña Mackenna L4A": 3},
    "Vicuña Mackenna L4A": {"Santa Julia": 3, "Vicuña Mackenna L4": 5},

    # Línea 5
    "Plaza de Maipú": {"Santiago Bueras": 2},
    "Santiago Bueras": {"Plaza de Maipú": 2, "Del Sol": 2},
    "Del Sol": {"Santiago Bueras": 2, "Monte Tabor": 2},
    "Monte Tabor": {"Del Sol": 2, "Las Parcelas": 2},
    "Las Parcelas": {"Monte Tabor": 2, "Laguna Sur": 3},
    "Laguna Sur": {"Las Parcelas": 3, "Barrancas": 2},
    "Barrancas": {"Laguna Sur": 2, "Pudahuel": 2},
    "Pudahuel": {"Barrancas": 2, "San Pablo L5": 3},
    "San Pablo L5": {"Pudahuel": 3, "Lo Prado": 2,"San Pablo L1": 5},
    "Lo Prado": {"San Pablo L5": 2, "Blanqueado": 2},
    "Blanqueado": {"Lo Prado": 2, "Gruta de Lourdes": 2},
    "Gruta de Lourdes": {"Blanqueado": 2, "Quinta Normal": 2},
    "Quinta Normal": {"Gruta de Lourdes": 2, "Cumming": 2},
    "Cumming": {"Quinta Normal": 2, "Santa Ana L5": 2},
    "Santa Ana L5": {"Cumming": 2, "Plaza de Armas L5": 2, "Santa Ana L2": 5},
    "Plaza de Armas L5": {"Santa Ana L5": 2, "Bellas Artes": 2, "Plaza de Armas L3": 5},
    "Bellas Artes": {"Plaza de Armas L5": 2, "Baquedano L5": 2},
    "Baquedano L5": {"Bellas Artes": 3, "Parque Bustamante": 2, "Baquedano L1": 5},
    "Parque Bustamante": {"Baquedano L5": 2, "Santa Isabel": 2},
    "Santa Isabel": {"Parque Bustamante": 2, "Irarrázaval L5": 2},
    "Irarrázaval L5": {"Santa Isabel": 2, "Ñuble L5": 3, "Irarrázaval L3": 5},
    "Ñuble L5": {"Irarrázaval L5": 3, "Rodrigo de Araya": 2, "Ñuble L6": 5},
    "Rodrigo de Araya": {"Ñuble L5": 2, "Carlos Valdovinos": 2},
    "Carlos Valdovinos": {"Rodrigo de Araya": 2, "Camino Agrícola": 2},
    "Camino Agrícola": {"Carlos Valdovinos": 2, "San Joaquín": 2},
    "San Joaquín": {"Camino Agrícola": 2, "Pedrero": 2},
    "Pedrero": {"San Joaquín": 2, "Mirador": 2},
    "Mirador": {"Pedrero": 2, "Bellavista de La Florida": 2},
    "Bellavista de La Florida": {"Mirador": 2, "Vicente Valdés L5": 3},
    "Vicente Valdés L5": {"Bellavista de La Florida": 3, "Vicente Valdés L4": 5},

    # Línea 6
    "Cerrillos": {"Lo Valledor":3},
    "Lo Valledor": {"Cerrillos": 3, "Pdte. Pedro Aguirre Cerda": 3},
    "Pdte. Pedro Aguirre Cerda":{"Lo Valledor": 3,"Franklin L6": 3},
    "Franklin L6": {"Pdte. Pedro Aguirre Cerda": 3, "Bio-Bío": 2, "Franklin L2": 5},
    "Bio-Bío": {"Franklin L6": 2, "Ñuble L6": 4},
    "Ñuble L6": {"Bio-Bío": 4, "Estadio Nacional": 4, "Ñuble L5": 5},
    "Estadio Nacional": {"Ñuble L6": 4, "Ñuñoa L6": 2},
    "Ñuñoa L6": {"Estadio Nacional": 2, "Inés de Suárez": 3, "Ñuñoa L3": 5},
    "Inés de Suárez": {"Ñuñoa L6": 3, "Los Leones L6": 5},
    "Los Leones L6": {"Inés de Suárez": 5,"Los Leones L1": 5}
}

F = nx.Graph()

#Añadir las conexiones entre las estaciones con sus respectivos tiempos
for estacion, conexiones in metro_opcion1.items():
    for destino, tiempo in conexiones.items():
        F.add_edge(estacion, destino, weight=tiempo)

metro_express = {
    # Línea 1
    "San Pablo L1": {"Neptuno": 2,"San Pablo L5": 5},
    "Neptuno": {"San Pablo L1": 2, "Pajaritos": 2},
    "Pajaritos": {"Neptuno": 2, "Las Rejas": 2},
    "Las Rejas": {"Pajaritos": 2, "Ecuador": 2},
    "Ecuador": {"Las Rejas": 2, "San Alberto Hurtado": 2},
    "San Alberto Hurtado": {"Ecuador": 2, "Universidad de Santiago": 2},
    "Universidad de Santiago": {"San Alberto Hurtado": 2, "Estación Central": 2},
    "Estación Central": {"Universidad de Santiago": 2, "U.L.A": 2},
    "U.L.A": {"Estación Central": 2, "República": 2},
    "República": {"U.L.A": 2, "Los Héroes L1": 2},
    "Los Héroes L1": {"República": 2, "La Moneda": 2, "Los Héroes L2": 5},
    "La Moneda": {"Los Héroes L1": 2, "Universidad de Chile L1": 2},
    "Universidad de Chile L1": {"La Moneda": 2, "Santa Lucía": 2, "Universidad de Chile L3": 5},
    "Santa Lucía": {"Universidad de Chile L1": 2, "Universidad Católica": 2},
    "Universidad Católica": {"Santa Lucía": 2, "Baquedano L1": 2},
    "Baquedano L1": {"Universidad Católica": 2, "Salvador": 2, "Baquedano L5": 5},
    "Salvador": {"Baquedano L1": 2, "Manuel Montt": 2},
    "Manuel Montt": {"Salvador": 2, "Pedro de Valdivia": 2},
    "Pedro de Valdivia": {"Manuel Montt": 2, "Los Leones L1": 2},
    "Los Leones L1": {"Pedro de Valdivia": 2, "Tobalaba L1": 2, "Los Leones L6": 5},
    "Tobalaba L1": {"Los Leones L1": 2, "El Golf": 2, "Tobalaba L4": 5},
    "El Golf": {"Tobalaba L1": 2, "Alcántara": 2},
    "Alcántara": {"El Golf": 2, "Escuela Militar": 2},
    "Escuela Militar": {"Alcántara": 2, "Manquehue": 2},
    "Manquehue": {"Escuela Militar": 2, "Hernando de Magallanes": 2},
    "Hernando de Magallanes": {"Manquehue": 2, "Los Dominicos": 3},
    "Los Dominicos": {"Hernando de Magallanes": 3},

    # Línea 2
    #luz roja
    "Hospital El Pino": {"Copa Lo Martínez": 3},
    "Copa Lo Martínez": {"Hospital El Pino": 3,"El Bosque": 5},
    "El Bosque": {"Copa Lo Martínez": 5,"La Cisterna L2": 2},
    "La Cisterna L2": {"El Bosque": 2,"Lo Ovalle": 4,"La Cisterna L4A": 5},
    "Lo Ovalle": {"La Cisterna L2": 4,"Ciudad del Niño": 2},
    "Ciudad del Niño": {"Lo Ovalle": 2,"Lo Vial": 3},
    "Lo Vial": {"Ciudad del Niño": 3,"El Llano": 2},
    "El Llano": {"Lo Vial": 3,"Franklin L2": 2},
    "Franklin L2": {"El Llano": 2,"Parque O'Higgins": 4,"Franlkin L6": 5},
    "Parque O'Higgins": {"Franklin L2": 4,"Los Héroes L2": 3},
    "Los Héroes L2": {"Parque O'Higgins": 3,"Santa Ana L2": 2,"Los Héroes L1": 5},
    "Santa Ana L2": {"Los Héroes L2": 2,"Puente Cal y Canto L2": 3,"Santa Ana L5": 5},
    "Puente Cal y Canto L2": {"Santa Ana L2": 3,"Patronato": 2,"Puente Cal y Canto L3": 5},
    "Patronato": {"Puente Cal y Canto L2": 2,"Cementerios": 3},
    "Cementerios": {"Patronato": 3,"Dorsal": 3},
    "Dorsal": {"Cementerios": 3,"Zapadores": 2},
    "Zapadores": {"Dorsal": 2,"Vespucio Norte": 2},
    "Vespucio Norte": {"Zapadores": 2},
    #luz verde
    "Hospital El Pino": {"Observatorio": 5},
    "Observatorio": {"Hospital El Pino": 5,"La Cisterna L2": 5},
    "La Cisterna L2": {"Observatorio": 5,"El Parrón": 3,"La Cistera L4A": 5},
    "El Parrón": {"La Cisterna L2": 3,"Lo Ovalle": 2},
    "Lo Ovalle": {"El Parrón": 2,"Departamental": 3},
    "Departamental": {"Lo Ovalle": 3,"San Miguel": 3},
    "San Miguel": {"Departamental": 3,"Franklin L2": 3},
    "Franklin L2": {"San Miguel": 3,"Rondizzoni": 2,"Franklin L6": 5},
    "Rondizzoni": {"Franklin L2": 2,"Toesca": 4},
    "Toesca": {"Rondizzoni": 4,"Los Héroes L2": 2},
    "Los Héroes L2": {"Toesca": 2,"Santa Ana L2": 2,"Los Héroes L1": 5},
    "Santa Ana L2": {"Los Héroes L2": 2,"Puente Cal y Canto L2": 3,"Santa Ana L5": 5},
    "Puente Cal y Canto L2": {"Santa Ana L2": 3,"Cerro Blanco": 3,"Puente Cal y Canto L3": 5},
    "Cerro Blanco": {"Puente Cal y Canto L2": 3,"Einstein": 3},
    "Einstein": {"Cerro Blanco": 3,"Zapadores": 3},
    "Zapadores": {"Einstein": 3,"Vespucio Norte": 2},
    "Vespucio Norte": {"Zapadores": 2},
    
    # Línea 3
    "Plaza Quilicura": {"Lo Cruzat": 2},
    "Lo Cruzat": {"Plaza Quilicura": 2, "Ferrocarril": 3},
    "Ferrocarril": {"Lo Cruzat": 3, "Los Libertadores": 3},
    "Los Libertadores": {"Ferrocarril": 3, "Cardenal Caro": 2},
    "Cardenal Caro": {"Los Libertadores": 2, "Vivaceta": 3},
    "Vivaceta": {"Cardenal Caro": 3, "Conchalí": 3},
    "Conchalí": {"Vivaceta": 3, "Plaza Chacabuco": 3},
    "Plaza Chacabuco": {"Conchalí": 3, "Hospitales": 3},
    "Hospitales": {"Plaza Chacabuco": 3, "Puente Cal y Canto L3": 3},
    "Puente Cal y Canto L3": {"Hospitales": 3, "Plaza de Armas L3": 2, "Puente Cal y Canto L2": 5},
    "Plaza de Armas L3": {"Puente Cal y Canto L3": 2, "Universidad de Chile L3": 2, "Plaza de Armas L5": 5},
    "Universidad de Chile L3": {"Plaza de Armas L3": 2, "Parque Almagro": 2, "Universidad de Chile L1": 5},
    "Parque Almagro": {"Universidad de Chile L3": 2, "Matta": 3},
    "Matta": {"Parque Almagro": 3, "Irarrázaval L3": 3},
    "Irarrázaval L3": {"Matta": 3, "Monseñor Eyzaguirre": 3, "Irarrázaval L5": 5},
    "Monseñor Eyzaguirre": {"Irarrázaval L3": 3, "Ñuñoa L3": 2},
    "Ñuñoa L3": {"Monseñor Eyzaguirre": 2, "Chile España": 2, "Ñuñoa L6": 5},
    "Chile España": {"Ñuñoa L3": 2, "Villa Frei": 3},
    "Villa Frei": {"Chile España": 3, "Plaza Egaña L3": 2},
    "Plaza Egaña L3": {"Villa Frei": 2, "Fernando Castillo Velasco": 3, "Plaza Egaña L4": 5},
    "Fernando Castillo Velasco": {"Plaza Egaña L3": 3},

    # Línea 4
    #Luz roja
    "Tobalaba L4": {"Francisco Bilbao": 3,"Tobalba L1": 5},
    "Francisco Bilbao": {"Tobalaba L4": 3,"Príncipe de Gales": 3},
    "Príncipe de Gales": {"Francisco Bilbao": 3,"Plaza Egaña L4": 3},
    "Plaza Egaña L4": {"Príncipe de Gales": 3,"Los Orientales": 2,"Plaza Egaña L3": 5},
    "Los Orientales": {"Plaza Egaña L4": 2,"Los Presidentes": 3},
    "Los Presidentes": {"Los Orientales": 3,"Las Torres": 3},
    "Las Torres": {"Los Presidentes": 3,"Macul": 2},
    "Macul": {"Las Torres": 2,"Vicuña Mackenna L4": 3},
    "Vicuña Mackenna L4": {"Macul": 3,"Vicente Valdés L4": 2,"Vicuña Mackenna L4A": 5},
    "Vicente Valdés L4": {"Vicuña Mackenna L4": 2,"Trinidad": 2,"Vicente Valdés L5": 5},
    "Trinidad": {"Vicente Valdés L4": 2,"Los Quillayes": 3},
    "Los Quillayes": {"Trinidad": 3,"Elisa Correa": 2},
    "Elisa Correa": {"Los Quillayes": 2,"Hospital Sótero del Río": 2},
    "Hospital Sótero del Río": {"Elisa Correa": 2,"Las Mercedes": 4},
    "Las Mercedes": {"Hospital Sótero del Río": 4,"Plaza de Puente Alto": 3},
    "Plaza de Puente Alto": {"Las Mercedes": 3},
    
    #Luz verde
    "Plaza de Puente Alto": {"Protectora de la Infancia": 4},
    "Protectora de la Infancia": {"Plaza de Puente Alto": 4,"Hospital Sótero del Río": 2},
    "Hospital Sótero del Río": {"Protectora de la Infancia": 2,"Elisa Correa": 2},
    "Elisa Correa": {"Hospital Sótero del Río": 2,"San José de la Estrella": 3},
    "San José de la Estrella": {"Elisa Correa": 3,"Rojas Magallanes": 3},
    "Rojas Magallanes": {"San José de la Estrella": 3,"Vicente Valdés L4": 2},
    "Vicente Valdés L4": {"Rojas Magallanes":2 ,"Vicuña Mackenna L4": 2,"Vicente Valdés L5": 5},
    "Vicuña Mackenna L4": {"Vicente Valdés L4": 2,"Macul": 3,"Vicuña Mackenna L4A": 5},
    "Macul": {"Vicuña Mackenna L4": 3,"Quilín": 4},
    "Quilín": {"Macul": 4,"Grecia": 3},
    "Grecia": {"Quilín": 3,"Plaza Egaña L4": 3},
    "Plaza Egaña L4": {"Grecia": 3,"Simón Bolivar": 2,"Plaza Egaña L3": 5},
    "Simón Bolivar": {"Plaza Egaña L4": 2,"Francisco Bilbao": 3},
    "Francisco Bilbao": {"Simón Bolivar": 3,"Cirstóbal Colón": 2},
    "Cirstóbal Colón": {"Francisco Bilbao": 2,"Tobalaba L4": 2},
    "Tobalaba L4": {"Cirstóbal Colón": 2,"Tobalba L1": 5},


    # Línea 4A
    "La Cisterna L4A": {"La Cisterna L2": 5, "San Ramón": 5},
    "San Ramón": {"La Cisterna L4A": 5, "Santa Rosa": 2},
    "Santa Rosa": {"San Ramón": 2, "La Granja": 4},
    "La Granja": {"Santa Rosa": 4, "Santa Julia": 2},
    "Santa Julia": {"La Granja": 2, "Vicuña Mackenna L4A": 3},
    "Vicuña Mackenna L4A": {"Santa Julia": 3, "Vicuña Mackenna L4": 5},

    # Línea 5
    #Luz roja
    "Plaza de Maipú": {"Santiago Bueras": 3},
    "Santiago Bueras": {"Plaza de Maipú": 3, "Monte Tabor": 3},
    "Monte Tabor": {"Santiago Bueras": 3, "Laguna Sur": 4},
    "Laguna Sur": {"Monte Tabor": 4, "Barrancas": 2},
    "Barrancas": {"Laguna Sur": 2, "Pudahuel": 2},
    "Pudahuel": {"Barrancas": 2, "San Pablo": 3},
    "San Pablo L5": {"Pudahuel": 3, "Blanqueado": 3,"San Pablo L1": 5},
    "Blanqueado": {"San Pablo L5": 3, "Quinta Normal": 4},
    "Quinta Normal": {"Blanqueado": 4, "Santa Ana L5": 4},
    "Santa Ana L5": {"Quinta Normal": 4, "Plaza de Armas L5": 2,"Santa Ana L2": 5},
    "Plaza de Armas L5": {"Santa Ana L5": 2, "Bellas Artes": 2,"Plaza de Armas L3": 5},
    "Bellas Artes": {"Plaza de Armas L5": 2, "Baquedano L5": 3},
    "Baquedano L5": {"Bellas Artes": 3, "Parque Bustamante": 2,"Baquedano L1": 5},
    "Parque Bustamante": {"Baquedano L5": 2, "Irarrázaval L5": 3},
    "Irarrázaval L5": {"Parque Bustamante": 3, "Ñuble L5": 3,"Irarrázaval L3": 5},
    "Ñuble L5": {"Irarrázaval L5": 3, "Rodrígo de Araya": 2,"Ñuble L6": 5},
    "Rodrígo de Araya": {"Ñuble L5": 2, "Camino Agrícola": 3},
    "Camino Agrícola": {"Rodrígo de Araya": 3, "San Joaquín": 2},
    "San Joaquín": {"Camino Agrícola": 2, "Mirador": 3},
    "Mirador": {"San Joaquín": 3, "Bellavista de La Florida": 2},
    "Bellavista de La Florida": {"Mirador": 2, "Vicente Valdés L5": 3},
    "Vicente Valdés L5": {"Bellavista de La Florida": 3,"Vicente Valdés L4": 5},
    
    #Luz verde
    "Plaza de Maipú": {"Del Sol": 3},
    "Del Sol": {"Plaza de Maipú": 3, "Las Parcelas": 3},
    "Las Parcelas": {"Del Sol": 3, "Laguna Sur": 3},
    "Laguna Sur": {"Las Parcelas": 3, "Pudahuel": 4},
    "Pudahuel": {"Laguna Sur": 4, "San Pablo L5": 3},
    "San Pablo L5": {"Pudahuel": 3, "Lo Prado": 2,"San Pablo L1": 5},
    "Lo Prado": {"San Pablo L5": 2, "Gruta de Lourdes": 4},
    "Gruta de Lourdes": {"Lo Prado": 4, "Cumming": 4},
    "Cumming": {"Gruta de Lourdes": 4, "Santa Ana L5": 2},
    "Santa Ana L5": {"Cumming": 2, "Plaza de Armas L5": 2,"Santa Ana L2": 5},
    "Plaza de Armas L5": {"Santa Ana L5": 2, "Bellas Artes": 2,"Plaza de Armas L3": 5},
    "Bellas Artes": {"Plaza de Armas L5": 2, "Baquedano L5": 3},
    "Baquedano L5": {"Bellas Artes": 3, "Santa Isabel": 3,"Baquedano L1": 5},
    "Santa Isabel": {"Baquedano L5": 3, "Irarrázaval L5": 2},
    "Irarrázaval L5": {"Santa Isabel": 2, "Ñuble L5": 3,"Irarrázaval L3": 5},
    "Ñuble L5": {"Irarrázaval L5": 3, "Carlos Valdovinos": 4,"Ñuble L6": 5},
    "Carlos Valdovinos": {"Ñuble L5": 4, "San Joaquín": 3},
    "San Joaquín": {"Carlos Valdovinos": 3, "Pedrero": 2},
    "Pedrero": {"San Joaquín": 2, "Bellavista de La Florida": 4},
    "Bellavista de La Florida": {"Pedrero": 4, "Vicente Valdés L5": 3},
    "Vicente Valdés L5": {"Bellavista de La Florida": 3,"Vicente Valdés L4": 5},

    # Línea 6
    "Cerrillos": {"Lo Valledor":3},
    "Lo Valledor": {"Cerrillos": 3, "Pdte. Pedro Aguirre Cerda": 3},
    "Pdte. Pedro Aguirre Cerda":{"Lo Valledor": 3,"Franklin L6": 3},
    "Franklin L6": {"Pdte. Pedro Aguirre Cerda": 3, "Bio-Bío": 2, "Franklin L2": 5},
    "Bio-Bío": {"Franklin L6": 2, "Ñuble L6": 4},
    "Ñuble L6": {"Bio-Bío": 4, "Estadio Nacional": 4, "Ñuble L5": 5},
    "Estadio Nacional": {"Ñuble L6": 4, "Ñuñoa L6": 2},
    "Ñuñoa L6": {"Estadio Nacional": 2, "Inés de Suárez": 3, "Ñuñoa L3": 5},
    "Inés de Suárez": {"Ñuñoa L6": 3, "Los Leones L6": 5},
    "Los Leones L6": {"Inés de Suárez": 5,"Los Leones L1": 5}
}
       
Ex = nx.Graph()

for estacion, conexiones in metro_express.items():
    for destino, tiempo in conexiones.items():
        Ex.add_edge(estacion, destino, weight=tiempo) 
        
##############################################################
def OrigenDestino_baja(hora_salida):
    EstacionOrigen = input("Por favor, escribe la estación de origen: ")
    EstacionDestino = input("Por favor, escribe la estación de destino: ")

    ruta_mas_corta = nx.shortest_path(F,EstacionOrigen,EstacionDestino, weight= tiempo)
    tiempo_de_ruta = nx.shortest_path_length(F,EstacionOrigen,EstacionDestino, weight = 'weight')

    # Inicializa el contador de transbordos
    contador_transbordos = 0

    # Almacena la línea de la primera estación para comparación
    linea_anterior = estaciones_lineas[ruta_mas_corta[0]]["linea"]

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la línea de la estación actual
        linea_actual = estaciones_lineas.get(estacion, {}).get("linea")

    # Si la línea actual es diferente de la anterior, es un transbordo
    if linea_actual and linea_actual != linea_anterior:
        contador_transbordos += 1  # Incrementa el contador de transbordos

    # Actualiza la línea anterior para la siguiente iteración
    linea_anterior = linea_actual
    
    #Imprimir la ruta mas corta
    print("La ruta más corte entre estaciones: ", ruta_mas_corta)
    print("Número de estaciones: ", len(ruta_mas_corta) - contador_transbordos)

    #Imprimir tiempo
    print("Tiempo estimado: ", tiempo_de_ruta) 
    plt.show()
    
    # Imprime el número total de transbordos
    print(f"Número de transbordos: {contador_transbordos}")
    
    hora = hora_salida.hour
    minutos = hora_salida.minute

    # Convertir la hora de salida a minutos totales
    minutos_totales_salida = hora * 60 + minutos

    # Considerar los transbordos (2 minutos adicionales por cada transbordo)
    tiempo_total_en_minutos = tiempo_de_ruta + contador_transbordos * 2

    # Calcular el tiempo exacto de llegada (sumando el tiempo de ruta y transbordos)
    minutos_totales_llegada = minutos_totales_salida + tiempo_total_en_minutos

    # Convertir los minutos totales de llegada a formato HH:MM
    hora_llegada = minutos_totales_llegada // 60
    minutos_llegada = minutos_totales_llegada % 60

    # Ajustar la hora si excede las 24 horas (si la llegada es al día siguiente)
    if hora_llegada >= 24:
        hora_llegada -= 24

    # Imprimir la hora de llegada
    print(f"Llegarás a las: {hora_llegada:02d}:{minutos_llegada:02d}")

##LLegada###
def OrigenDestino_baja_llegada(hora_llegada):
    EstacionOrigen = input("Por favor, escribe la estación de origen: ")
    EstacionDestino = input("Por favor, escribe la estación de destino: ")

    ruta_mas_corta = nx.shortest_path(F, EstacionOrigen, EstacionDestino, weight=tiempo)
    tiempo_de_ruta = nx.shortest_path_length(F, EstacionOrigen, EstacionDestino, weight='weight')

    # Inicializa el contador de transbordos
    contador_transbordos = 0

    # Almacena la línea de la primera estación para comparación
    linea_anterior = estaciones_lineas[ruta_mas_corta[0]]["linea"]

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la línea de la estación actual
        linea_actual = estaciones_lineas.get(estacion, {}).get("linea")

        # Si la línea actual es diferente de la anterior, es un transbordo
        if linea_actual and linea_actual != linea_anterior:
            contador_transbordos += 1  # Incrementa el contador de transbordos

        # Actualiza la línea anterior para la siguiente iteración
        linea_anterior = linea_actual
    
    # Imprimir la ruta más corta
    print("La ruta más corta entre estaciones: ", ruta_mas_corta)
    print("Número de estaciones: ", len(ruta_mas_corta) - contador_transbordos)

    # Imprimir tiempo
    print("Tiempo estimado: ", tiempo_de_ruta) 
    plt.show()
    
    # Imprime el número total de transbordos
    print(f"Número de transbordos: {contador_transbordos}")

    # Calcular la hora de salida
    hora = hora_llegada.hour
    minutos = hora_llegada.minute
    tiempo_total_en_minutos = tiempo_de_ruta + contador_transbordos * 2  # Considera tiempo de transbordos si es necesario
    minutos_totales = hora * 60 + minutos - tiempo_total_en_minutos  # Restar el tiempo de ruta en minutos

    # Convertir de nuevo a formato HH:MM
    hora_salida = minutos_totales // 60
    minutos_salida = minutos_totales % 60

    # Ajustar la hora si es negativa
    if minutos_totales < 0:
        print("No es posible calcular la hora de salida.")
    else:
        # Asegúrate de que la hora_salida esté dentro del rango
        if hora_salida < 0:
            hora_salida += 24  # Sumar 24 horas si la hora de salida es negativa

        print(f"Debes salir a las: {hora_salida:02d}:{minutos_salida:02d}")
    
    
#########################################################
    
    
def OrigenDestino_express(hora_salida):

    # Solicita las estaciones de origen y destino
    EstacionOrigen = input("Por favor, escribe la estación de origen: ")
    EstacionDestino = input("Por favor, escribe la estación de destino: ")

    # Encuentra la ruta más corta y su tiempo usando el grafo
    ruta_mas_corta = nx.shortest_path(Ex, EstacionOrigen, EstacionDestino, weight='tiempo')
    tiempo_de_ruta = nx.shortest_path_length(Ex, EstacionOrigen, EstacionDestino, weight='weight')

    ################## Inicializa el contador de transbordos
    contador_transbordos = 0

    # Almacena la línea de la primera estación para comparación
    linea_anterior = estaciones_lineas[ruta_mas_corta[0]]["linea"]

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la línea de la estación actual
        linea_actual = estaciones_lineas.get(estacion, {}).get("linea")

        # Si la línea actual es diferente de la anterior, es un transbordo
        if linea_actual and linea_actual != linea_anterior:
            contador_transbordos += 1  # Incrementa el contador de transbordos

        # Actualiza la línea anterior para la siguiente iteración
        linea_anterior = linea_actual
    ################ Fin contador transbordos

    # Guarda el color de luz anterior para detectar cambios
    luz_anterior = estaciones_lineas[ruta_mas_corta[0]].get("luz")

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la luz de la estación actual
        luz_actual = estaciones_lineas.get(estacion, {}).get("luz")  # Esto devuelve None si "luz" no existe

        # Si hay un cambio de luz y la luz actual no es None
        if luz_actual is not None and luz_anterior is not None:
            # Compara las luces
            if set(luz_anterior) != set(luz_actual):
                tiempo_de_ruta += 2  # Añade 2 minutos por el cambio de luz

        # Actualiza la luz anterior para la siguiente iteración
        luz_anterior = luz_actual
    ############## Fin tiempo total con cambio de andén

    # Imprimir la ruta más corta
    print("La ruta más corta entre estaciones: ", ruta_mas_corta)
    print("Número de estaciones: ", len(ruta_mas_corta) - contador_transbordos)

    # Imprimir tiempo
    print("Tiempo estimado: ", tiempo_de_ruta)

    # Imprimir el número total de transbordos
    print(f"Número de transbordos: {contador_transbordos}")

    ###### Calcular la hora de llegada ######
    # Descomponer la hora de salida ingresada por el usuario
    
    hora = hora_salida.hour
    minutos = hora_salida.minute

    # Convertir la hora de salida a minutos totales
    minutos_totales_salida = hora * 60 + minutos

    # Considerar los transbordos (2 minutos adicionales por cada transbordo)
    tiempo_total_en_minutos = tiempo_de_ruta + contador_transbordos * 2

    # Calcular el tiempo exacto de llegada (sumando el tiempo de ruta y transbordos)
    minutos_totales_llegada = minutos_totales_salida + tiempo_total_en_minutos

    # Convertir los minutos totales de llegada a formato HH:MM
    hora_llegada = minutos_totales_llegada // 60
    minutos_llegada = minutos_totales_llegada % 60

    # Ajustar la hora si excede las 24 horas (si la llegada es al día siguiente)
    if hora_llegada >= 24:
        hora_llegada -= 24

    # Imprimir la hora de llegada
    print(f"Llegarás a las: {hora_llegada:02d}:{minutos_llegada:02d}")
    

#LLegada#######
def OrigenDestino_express_llegada(hora_llegada):

    
    # Solicitar las estaciones de origen y destino
    EstacionOrigen = input("Por favor, escribe la estación de origen: ")
    EstacionDestino = input("Por favor, escribe la estación de destino: ")

    # Encontrar la ruta más corta y el tiempo usando el grafo
    ruta_mas_corta = nx.shortest_path(Ex, EstacionOrigen, EstacionDestino, weight='weight')
    tiempo_de_ruta = nx.shortest_path_length(Ex, EstacionOrigen, EstacionDestino, weight='weight')

    # Inicializa el contador de transbordos
    contador_transbordos = 0

    # Almacena la línea de la primera estación para comparación
    linea_anterior = estaciones_lineas[ruta_mas_corta[0]]["linea"]

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la línea de la estación actual
        linea_actual = estaciones_lineas.get(estacion, {}).get("linea")

        # Si la línea actual es diferente de la anterior, es un transbordo
        if linea_actual and linea_actual != linea_anterior:
            contador_transbordos += 1  # Incrementa el contador de transbordos

        # Actualiza la línea anterior para la siguiente iteración
        linea_anterior = linea_actual

    # Guarda el color de luz anterior para detectar cambios
    luz_anterior = estaciones_lineas[ruta_mas_corta[0]].get("luz")

    # Recorre la ruta desde la segunda estación
    for estacion in ruta_mas_corta[1:]:
        # Obtiene la luz de la estación actual
        luz_actual = estaciones_lineas.get(estacion, {}).get("luz")

        # Si hay un cambio de luz y la luz actual no es None
        if luz_actual is not None and luz_anterior is not None:
            # Compara las luces
            if set(luz_anterior) != set(luz_actual):
                tiempo_de_ruta += 2  # Añade 2 minutos por el cambio de luz

        # Actualiza la luz anterior para la siguiente iteración
        luz_anterior = luz_actual

    # Imprimir la ruta más corta
    print("La ruta más corta entre estaciones: ", ruta_mas_corta)
    print("Número de estaciones: ", len(ruta_mas_corta) - contador_transbordos)

    # Imprimir tiempo
    print("Tiempo estimado: ", tiempo_de_ruta)

    # Imprime el número total de transbordos
    print(f"Número de transbordos: {contador_transbordos}")

    # Calcular la hora de salida
    
    hora = hora_llegada.hour
    minutos = hora_llegada.minute
    
    tiempo_total_en_minutos = tiempo_de_ruta + contador_transbordos * 2  # Considera tiempo de transbordos
    minutos_totales = hora * 60 + minutos - tiempo_total_en_minutos  # Restar el tiempo de ruta en minutos

    # Convertir de nuevo a formato HH:MM
    hora_salida = minutos_totales // 60
    minutos_salida = minutos_totales % 60

    # Ajustar la hora si es negativa
    if minutos_totales < 0:
        print("No es posible calcular la hora de salida.")
    else:
        if hora_salida < 0:
            hora_salida += 24  # Sumar 24 horas si la hora de salida es negativa

        print(f"Debes salir a las: {hora_salida:02d}:{minutos_salida:02d}")