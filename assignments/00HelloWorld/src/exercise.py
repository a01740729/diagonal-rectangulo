import math
def main():
    #escribe tu código abajo de esta línea
    pass

    a = float(input('Dame el ancho del rectangulo: '))
    l = float(input('Dame el largo del rectangulo: '))

    d = math.sqrt ((a ** 2) + (l ** 2))

    print('La diagonal es: '+str(d))

if __name__=='__main__':
    main()
