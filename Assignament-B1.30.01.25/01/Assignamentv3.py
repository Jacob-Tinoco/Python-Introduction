#Sobre Números largos, de grandes cantidades
# Población = 1,000,000.00
"""
Sobre la línea con la variable Población del código:
Población = 1,000,000.00
Python interpreta esto de una manera que podría ser diferente a lo que esperas. En Python, 
cuando usas comas entre números, NO ESTAS ESCRIBIENDO UN NUMERO con formato de miles (como 1,000,000.00), 
sino que estás creando una tupla con tres elementos:

El número 1
El número 0
El número 0.0
Por lo tanto, Población será una tupla con el valor (1, 0, 0.0)
"""
#A continuación se muestran formas correctas:
"""
Formas correctas de escribir un millón:
Población = 1000000.00  # Sin comas
o
Población = 1_000_000.00  # Usando guiones bajos para mejor legibilidad (Python 3.6+)
Los guiones bajos (_) en números son una característica de Python que permite hacer los 
números grandes más legibles sin afectar su valor. Es una buena práctica usarlos cuando
trabajas con números grandes.
"""
# Asignación de variables
#Imprimir números de múltiples cifras
Ciudad = "CDMX" #22,505,300
Población = 22,505,300
poblacion_con_comas = 22,505,300
poblacion_correcta = 22505300
poblacion_con_guiones = 22_505_300

# Texto base para evitar repetición
base_texto = "{} tiene {} de personas, según: worldpopulationreview (2024)"

# Imprimir las diferentes representaciones de la población
print(f"\nRepresentaciones de la población de {Ciudad}:")
print("Imprimimos los datos numericos con los siguientes metodos")
print(f"1. Con comas    : {base_texto.format(Ciudad, poblacion_con_comas)} \n   Tipo: {type(poblacion_con_comas)}")
print(f"2. Sin comas    : {base_texto.format(Ciudad, poblacion_correcta)} \n   Tipo: {type(poblacion_correcta)}")
print(f"3. Con guiones  : {base_texto.format(Ciudad, poblacion_con_guiones)} \n   Tipo: {type(poblacion_con_guiones)}")