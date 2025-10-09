# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "polars",
# ]
# ///

import polars as pl # type: ignore


def main() -> None:
    df = pl.read_csv('C:/Users/Jhonm/repos/scripts/prog1/datos.csv')
    
    df2 = df.filter(
        pl.col('kilometraje') < 50_000
    )

    print(df2)


if __name__ == "__main__":
    main()
