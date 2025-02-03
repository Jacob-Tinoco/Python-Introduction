## Autores

- **Jacob Tinoco** - *Repositorio de educación* - [Jacob-Tinoco](https://github.com/Jacob-Tinoco)
## Bienvenida
¡Hola! 👋 Bienvenido a la carpeta **Lección de Assignament**, aqui se aprendera como asignar valores en python y como imprimir información básica: números y texto.

## Desclamer 
 Se permite la divulgación de estas lecciones con fines educativos y se prohibe su uso para fines de lucro, no olviden contribuir de una u otra manera, recomendando, dando sugerencias o simplemente mencionandome.

# Assignament

## Sobre la lección

Esta lección cubre los conceptos básicos de la asignación en Python, incluyendo cómo utilizar el operador `=` para asignar valores a variables, realizar asignaciones múltiples, intercambiar valores, y más.

## Para qué se usa el assignament

El assignament se utiliza para enseñar a los estudiantes cómo asignar valores a variables en Python y cómo manejar diferentes tipos de asignaciones, lo cual es fundamental para cualquier programación en Python.
## Lección

La asignación básica Utiliza el operador `=` para asignar un valor a una variable.

- Ejemplo:
    
    ```python
    x = 10
    y = "Hola"
    z = 3.14
    
    ```
    

**Asignación Múltiple**: Puedes asignar valores a múltiples variables en una sola línea.

- Ejemplo:
    
    ```python
    a, b, c = 1, 2, 3
    
    ```
    

**Intercambio de Valores**: Puedes intercambiar los valores de dos variables sin necesidad de una variable temporal.

- Ejemplo:
    
    ```python
    x, y = y, x
    
    ```
    

**Asignación a Estructuras de Datos**: Puedes asignar valores a elementos de listas, tuplas, diccionarios, etc.

- Ejemplo:
    
    ```python
    lista = [1, 2, 3]
    lista[0] = 10  # Cambia el primer elemento de la lista a 10
    
    diccionario = {"nombre": "Juan", "edad": 30}
    diccionario["edad"] = 31  # Cambia el valor asociado a la clave "edad" a 31
    
    ```
    

**Asignación con Desempaquetado**: Puedes desempaquetar elementos de una lista o tupla y asignarlos a variables.

- Ejemplo:
    
    ```python
    tupla = (1, 2, 3)
    x, y, z = tupla  # Asigna 1 a x, 2 a y, y 3 a z
    
    ```
    

**Asignación con Operadores Compuestos**: Puedes utilizar operadores compuestos para realizar operaciones y asignar el resultado a la misma variable.

- Ejemplo:
    
    ```python
    x = 5
    x += 3  # Equivalente a x = x + 3, ahora x es 8
    x *= 2  # Equivalente a x = x * 2, ahora x es 16
    x %= 3
    
    ```
## Requerimientos Básicos

Para seguir esta lección, necesitarás tener instalado Python en tu sistema. Además, se recomienda tener un editor de texto o un entorno de desarrollo integrado (IDE) como Visual Studio Code o PyCharm.

## Código de Instalación de los Requerimientos para el CMD en Linux

Para instalar Python, puedes seguir estos pasos en la línea de comandos (CMD):

```bash


# Actualiza el gestor de paquetes
sudo apt update

# Instala Python
sudo apt install python3

# Verifica la instalación
python3 --version
```

## Código de Instalación de los Requerimientos para el CMD en Linux
## Instalación de Python en Windows

Para instalar Python en Windows, sigue estos pasos:

1. **Descargar el instalador de Python**:
   - Ve al sitio web oficial de Python: [python.org](https://www.python.org/)
   - Haz clic en el botón "Download Python" para descargar el instalador.

2. **Ejecutar el instalador**:
   - Abre el archivo descargado para iniciar el instalador.
   - Asegúrate de marcar la casilla "Add Python to PATH" antes de hacer clic en "Install Now".

3. **Verificar la instalación**:
   - Abre el símbolo del sistema (CMD).
   - Escribe el siguiente comando para verificar que Python se ha instalado correctamente:
     ```bash
     python --version
     ```
   - Deberías ver la versión de Python instalada en tu sistema.

4. **Instalar pip (si no está incluido)**:
   - Pip es el gestor de paquetes de Python y generalmente se incluye con la instalación de Python. Para verificar si pip está instalado, ejecuta el siguiente comando:
     ```bash
     pip --version
     ```
   - Si pip no está instalado, puedes instalarlo manualmente siguiendo las instrucciones en el sitio web oficial de Python.

5. **Actualizar pip**:
   - Es recomendable actualizar pip a la última versión. Ejecuta el siguiente comando:
     ```bash
     python -m pip install --upgrade pip
     ```

Con estos pasos, tendrás Python instalado y listo para usar en tu sistema Windows.

---

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jacob-t-329675258/) o en [Instagram](https://www.instagram.com/jknc.0/).

## Autor

Jacob Tinoco
