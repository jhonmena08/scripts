
def sumar(n1: int, n2: int) -> int:
    return n1 + n2


def sumar2(n1, n2):
    return n1 + n2


def mostrar_name() -> str:
    print(__name__)


def tipos_datos_python() -> None:
    edad: int = 32
    salario: float = 1523.56
    is_hombre: bool = True
    colores: list = ['rojo', 'verde', 'amarillo']
    coordenada: tuple = (100, 200)
    conjuntos: set = {'a', 'b', 'c', 'a', 'a' }

    print(edad)
    print(salario)
    print(is_hombre)
    print(colores)
    print(coordenada)
    print(conjuntos)

    # ciclo for
    for e in colores:
        print(e)


def ciclo_white() -> None:

    counter: int = 0
    while True:
        print(counter)
        counter = counter + 1
