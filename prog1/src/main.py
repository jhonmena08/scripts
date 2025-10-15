from pyproj import Transformer


# WGS84 lat/lon (EPSG:4326)
# MAGNA-SIRGAS Cali (EPSG:6249)
# WGS84/UTM Zona 18 N (EPSG:32618)
# MAGNA-SIRGAS Origen Oeste (EPSG:3115)
# MAGNA-SIRGAS CTM12 (EPSG:9377)

def tranformar_coordenadas() -> int:
    # Coordenadas WGS84
    lat, lon = 3.44188333333, -76.5205625

    # Magna-Cali 2009
    # norte, este = 872364.630, 1061900.180

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:6249")
    y, x = transformer.transform(lat, lon)
    print(f"Coordenadas: norte = {y:.5f}, este = {x:.5f}")

    return 0



def main():
    tranformar_coordenadas()
    


if __name__ == "__main__":
    main()
