#Sobre números largos, de grandes cantidades
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
# Para ver la diferencia:
poblacion_con_comas = 1,000,000.00
poblacion_correcta = 1000000.00
poblacion_con_guiones = 1_000_000.00

print(f"Con comas (crea una tupla): {poblacion_con_comas}, tipo: {type(poblacion_con_comas)}")
print(f"Sin comas (número correcto): {poblacion_correcta}, tipo: {type(poblacion_correcta)}")
print(f"Con guiones bajos (número correcto): {poblacion_con_guiones}, tipo: {type(poblacion_con_guiones)}")


