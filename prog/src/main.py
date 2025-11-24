from pyproj import Transformer
import pandas as pd
from libtopo.cogo import Point, acimut_dist

import os



def transformar(origen: str, dest: str, lat: float, lon: float, h: float) -> tuple[float, float]:
    tf = Transformer.from_crs(origen, dest, always_xy=True)
    x, y, z = tf.transform(lat, lon, h)
    return (x, y, z)

# end


def get_coord_geodesica(puntos: list[Point]) -> None:
    for p in puntos:
        # Magna Cali -> WGS84
        x, y, z = transformar(
        "EPSG:6249", "EPSG:4326", p.x, p.y, 0.0)

        print(f'|{x:^15.9f}|{y:^15.9f}|{p.descripcion:^15}|')

# end


def calcular_acimut_dist(puntos: list[Point]) -> None:
    for idx in range(len(puntos) - 1):
        az_dist: tuple[str, float] =  acimut_dist(puntos[idx],  puntos[idx + 1])
        vertices: str = str(puntos[idx].descripcion) + ' -> ' + str(puntos[idx + 1].descripcion)
        print(f'|{az_dist[0]:^12}|{az_dist[1]:10.3f}|{vertices:^25}|')

# end


def get_point(row: tuple) -> Point:
    return Point(row['E1'], row['N1'], row['vertice'])

# end


def main() -> int:
    os.system('cls')

    df = pd.read_excel('ptos_control_cali.xlsx')

    # filtrar
    df = df[df['ubicacion'].str.contains('autonoma')][['N1', 'E1', 'vertice']]

    # obtener la lista de Puntos
    ptos = [r for r in df.apply(get_point, axis=1)]

    get_coord_geodesica(ptos)
    print()

    return 0



if __name__ == "__main__":
    main()
