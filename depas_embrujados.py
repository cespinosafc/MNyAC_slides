# Calcular el costo total de los departamentos que pueden
# y quieren rentar.
# Restricciones:
# Entrada:
#     - Una matriz (una lista de listas) donde cada entrada
#        represente el costo del depa. Aquellos que estan
#        embrujados tienen un costo 0
#         La matriz es de dimensiones n x m donde:
#         1 < n < 5
#         1 < m < 5
#         El costo costo maximo de un depa puede ser 10
# Salida:
#     - Numero entero que represente el precio total de todos
#       los cuartos que pueden rentar
# Tiempo de ejecución: menor a 4 seg

def costo_depas(matriz):
    resultado = 0
    n = len(matriz)
    m = len(matriz[0])
    for ind_col in range(m):
        for ind_fil in range(n):
            if matriz[ind_fil][ind_col] == 0:
                break
            resultado = resultado + matriz[ind_fil][ind_col]
    return resultado
