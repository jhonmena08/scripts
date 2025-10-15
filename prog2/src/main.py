import os
import polars as pl


def main():
    os.system('cls')

    # df = pl.read_csv('C:/Users/Jhonm/repos/scripts/prog2/autos.csv', try_parse_dates=True)
    df = pl.read_csv('C:/Users/Jhonm/repos/scripts/prog2/autos.csv')
    

    # df2 = df.filter(
    #     pl.col('modelo') == 'Picanto',
    #     pl.col('kilometraje') < 50_000,
    #     pl.col('transmision') == 'Manual',
    #     pl.col('anio') > 2019
    # )

    # convertir a mayuscula los nombres columnas
    # df2 = df.select(
    #     pl.all().name.map(lambda e: e.upper())
    # )

    # convertir columnas Date y Float
    df2 = df.with_columns(
        pl.col('fecha_venta').cast(pl.Date),
        pl.col('precio').cast(pl.Float64)
    )

    # extraer año, mes, dia
    # df2 = df2.with_columns(
    #     pl.col('fecha_venta').dt.year().alias('año'),
    #     pl.col('fecha_venta').dt.month().alias('mes'),
    #     pl.col('fecha_venta').dt.day().alias('dia'),
    # )

    df2 = df2.select(
        pl.col('modelo').first()
    )
    print(df2)

    

if __name__ == "__main__":
    main()
