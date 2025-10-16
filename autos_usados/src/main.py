import polars as pl
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def get_data() -> pl.DataFrame:
    data =  pl.read_csv('C:/Users/Jhonm/repos/scripts/autos_usados/autos.csv', try_parse_dates=True)

    # convertir columna a float
    data = data.with_columns(
        pl.col('precio').cast(pl.Float32)
    )

    return data


def predecir(df: pl.DataFrame) -> None:
    # ===============================================
    # definir predictoras y objetivo
    # ===============================================
    features: list = ['modelo', 'anio', 'kilometraje']
    target: list = ['precio']

    # Convertir a pandas para Scikit-learn
    data = df[features + target].to_pandas()

    # ================================================
    # dividir datos entrenamiento (80%) y prueba (20%)
    # ================================================
    X = data[features]
    Y = data[target]

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=0) 

    # ===============================================
    # definir preprocesamiento
    # ===============================================
    categoria_features = ['modelo']
    numeric_features = ['anio', 'kilometraje']

    preprocesamiento = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categoria_features),
            ('num', 'passthrough', numeric_features)
        ]
    )

    # ==============================================
    # crear modelo Random Forest
    # ==============================================
    model = Pipeline(steps=[
        ('preprocessor', preprocesamiento),
        ('regressor', RandomForestRegressor(n_estimators=200, random_state=42))

    ])
    
    # ============================================
    # Entrenar
    # ============================================
    model.fit(x_train, y_train)

    # ===========================================
    # Evaluacion del modelo
    # ===========================================
    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # ==========================================
    # Predicion de un nuevo auto
    # ==========================================
    nuevo_auto = {
        'modelo': ['Picanto'],
        'anio': [2021],
        'kilometraje': [60_000]
    }

    print(f'\nCoeficiente de determinacion (R**2): {r2:.3f}')
    prediccion = model.predict(pl.DataFrame(nuevo_auto).to_pandas())
    print(f'Precio estimado del {nuevo_auto['modelo']} con {nuevo_auto['kilometraje']} km del año {nuevo_auto['anio']} es de: ${prediccion[0]:,.0f}\n')



def main() -> int:
    os.system('cls')

    df = get_data()
    predecir(df)

    df2 = df.filter(
        pl.col('modelo') == 'Picanto'
    )

    print(df2)

    return 0


if __name__ == "__main__":
    main()
