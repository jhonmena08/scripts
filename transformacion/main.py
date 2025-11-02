# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyproj",
# ]
# ///

from pyproj import Transformer


def main() -> int:
    # Magna-Cali -> CTM12
    tf = Transformer.from_crs('EPSG:6249', 'EPSG:9377', always_xy=True )
    
    e, n = 1061912.027, 862535.415

    x, y = tf.transform(e, n)
    print(f'x:{x}, y:{y}')

    return 0


if __name__ == '__main__':
    main()
