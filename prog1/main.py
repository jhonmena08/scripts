# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "polars",
# ]
# ///

import os
import polars as pl # type: ignore


def main() -> None:
    os.system('cls')

    df = pl.read_csv('C:/Users/Jhonm/repos/scripts/prog1/datos.csv')

    # convertir columna a Float
    df = df.with_columns(
        pl.col('price').cast(pl.Float64)
    )

    df = df.with_columns(
        pl.col('product').str.split(' ').list.get(0).alias('marca'),
        pl.col('product').str.split(' ').list.get(1).alias('linea')
    )

    print(df.head(5))

    # print(df.select(
    #     pl.col('product')
    # ).unique())



if __name__ == "__main__":
    main()
