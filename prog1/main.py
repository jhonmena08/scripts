# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "polars",
# ]
# ///

import polars as pl # type: ignore


def main() -> None:
    df = pl.read_csv('C:/Users/Jhonm/prog1/datos.csv')
    print(df)


if __name__ == "__main__":
    main()
