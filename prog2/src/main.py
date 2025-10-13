import os
import polars as pl


def main():
    os.system('cls')

    df = pl.read_csv('C:/Users/Jhonm/repos/scripts/prog2/autos.csv')
    # df.write_csv('C:/Users/Jhonm/repos/scripts/prog2/autos3.csv')

    df2 = df.filter(
        pl.col('modelo') == 'Picanto',
        pl.col('kilometraje') < 50_000,
        pl.col('transmision') == 'Manual',
        pl.col('anio') > 2020
    )

    print(df2)

    

if __name__ == "__main__":
    main()
