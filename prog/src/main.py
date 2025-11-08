from topo.cogo import Point, acimut_dist
import pandas as pd
import os


def get_point(row: tuple) -> Point:
    return Point(row['E1'], row['N1'], row['vertice'])



def main() -> int:
    os.system('cls')

    df = pd.read_excel('ptos_control_cali.xlsx')

    # filtrar
    # df = df[df['ubicacion'].str.contains('autonoma')][['N1', 'E1', 'vertice']]
    puntos = [fila for fila in df.apply(get_point, axis=1)]


    # calcular y mostrar acimut y distancia
    for idx in range(len(puntos) - 1):
        az_dist: tuple[str, float] =  acimut_dist(puntos[idx],  puntos[idx + 1])
        vertices: str = str(puntos[idx].descripcion) + ' -> ' + str(puntos[idx + 1].descripcion)

        print(f'|{az_dist[0]:^12}|{az_dist[1]:10.3f}|{vertices:^25}|')

    print()
    return 0


if __name__ == "__main__":
    main()
