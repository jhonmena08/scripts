from topo.cogo import Point, acimut_dist
import pandas as pd
import os


def get_point(row: tuple) -> Point:
    return Point(row['x'], row['y'])



def main() -> int:
    os.system('cls')

    df = pd.read_csv('ptos.csv')
    puntos = [fila for fila in df.apply(get_point, axis=1)]


    # df2 = pd.DataFrame({
    #     'location': puntos
    # })

    # calcular acimut y distancia
    for idx in range(len(puntos) - 1):
        print(f'{acimut_dist(puntos[idx],  puntos[idx + 1])}\t{puntos[idx].descripcion} -> {puntos[idx + 1].descripcion}')


    print()
    return 0


if __name__ == "__main__":
    main()
