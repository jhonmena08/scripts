from topo.cogo import Point, distancia
import pandas as pd
import os


def main() -> int:
    os.system('cls')
    
    df = pd.DataFrame({
        'location': [Point(100, 200), Point(500,456), Point(199, 87, 'cer'), Point(344.52, 233.04)]
    })

    print(df)

    return 0


if __name__ == "__main__":
    main()
