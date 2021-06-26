# Hacer un programa que, dado un año, calcule el siglo que le
# corresponde
# Entrada:
#     - Un valor entero que representa el año 1 <= year <= 2500
# Salida:
#     - Un valor que represente el siglo del año en cuestion

def siglo(year):
    resul = int(year/100)+1
    return resul
