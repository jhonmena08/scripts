# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyproj",
# ]
# ///

from pyproj import Transformer # type: ignore



def transformar(origen: str, dest: str, lat: float, lon: float, h: float) -> tuple[float, float]:
    tf = Transformer.from_crs(origen, dest, always_xy=True )
    x, y, z = tf.transform(lat, lon, h)
    return (x, y, z)



def main() -> int:

    # Magna-Cali -> CTM12
    # x, y, z = transformar('EPSG:6249', 'EPSG:9377', 1061912.027, 862535.415, 0.00)

    # Geocentricas wgs84 -> Magna-Cali
    x, y, z = transformar('EPSG:4328', 'EPSG:6249', 1483099.97741, -6193060.17470, 373124.22773)

    print(f'x:{x}, y:{y}, z:{z}')

    return 0



if __name__ == '__main__':
    main()
