# Hacer un programa que calcule el area de la figura
# dibujada
# Restricciones:
# Entrada:
#     - numero entero 1<n<10^5
# Salida
#     - numero entero que representa el area de la figura
#       n-enesima
# Tiempo de ejecución
#     - limite: 4 seg

def area(n):
    resul = n**2 + (n-1)**2
    return resul
