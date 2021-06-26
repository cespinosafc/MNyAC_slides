# Hacer un programa que revise una string es un palindromo
# Restricciones:
# Entrada:
#     - Debe de recibir una string no vacia, en minisculas y sin espacios
#      -   1<len(entrada)<10^5
# Salida:
#     - Debe de regresar True o False

def palindromo(entrada):
    entrada_inv = entrada[::-1]
    if entrada == entrada_inv:
        return True
    else:
        return False
