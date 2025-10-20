import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import os


pl.Config(float_precision=3)

def get_data() -> pl.DataFrame:
    return pl.read_excel('C:/Users/Jhonm/repos/scripts/curva_s/cronograma.xlsx')


def depurar_datos(df: pl.DataFrame) -> pl.DataFrame:
    # convertir a minuscula
    data = df.with_columns(
        pl.col("actividad").str.to_lowercase()
    )

    # obtener fechas de inicio unicas 
    data = data.unique(subset=['inicio'])

    # agregar columna duracion en dias
    data = data.with_columns(
        (pl.col('fin') - pl.col('inicio')).dt.total_days().alias('duracion')
    )

    # frecuencia acumulada
    data = data.with_columns(
        pl.col('duracion').cum_sum().alias('acumulada')
    )

    val_max = data['acumulada'].max()
    fecha_max = data['fin'].max()
    fecha_min = data['inicio'].min()

    print(fecha_max - fecha_min)

    # frecuencia acumulada en %
    data = data.with_columns(
        ((pl.col('acumulada') / val_max) * 100).alias('acumulada_%')
    )

    return data


def graficar(datos: pl.DataFrame) -> None:
    # grey grid in the background:
    sns.set_theme(style="darkgrid")
    sns.lineplot(data=datos, x='actividad', y='acumulada_%')
    plt.xticks(rotation=90)
    plt.show()
    return 



def main() -> int:
    os.system('cls')

    df = get_data()
    datos = depurar_datos(df)

    print(datos) 
    graficar(datos)


    return 0


if __name__ == "__main__":
    main()
