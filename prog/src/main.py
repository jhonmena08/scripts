from topo.cogo import Point, distancia


def main():
    p1 = Point(100.05, 213.74, 'gps1')
    p2 = Point(153.98, 199.66, 'gps2')

    print(f'{p1}\n{p2}')
    print(f'{distancia(p1, p2):.4f} mts')


if __name__ == "__main__":
    main()
