# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyproj",
# ]
# ///

from pyproj import Transformer  # type: ignore


def transformar(origen: str, dest: str, lat: float, lon: float, h: float) -> tuple[float, float]:
    tf = Transformer.from_crs(origen, dest, always_xy=True)
    x, y, z = tf.transform(lat, lon, h)
    return (x, y, z)



def main() -> int:
    # magna-cali -> ctm12
    # x, y, z = transformar('EPSG:6249', 'EPSG:9377', 1061912.027, 862535.415, 0.00)

    # geocentricas wgs84 -> magna-cali
    x, y, z = transformar(
        "EPSG:4328", "EPSG:6249", 1484438.02386, -6192868.80262, 370607.90097
    )

    print(f"x:{x}, y:{y}, z:{z}")
    return 0



if __name__ == "__main__":
    main()
