print('El __name__ de este archivo es: {}'.format(__name__))

if __name__ == "__main__":
    print("Este archivo esta siendo ejecutado directamente")
else:
    print("Este archivo esta siendo importado")
