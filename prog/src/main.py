import topo.cogo as cogo


def main():
    p1 = cogo.Point(100.05, 213.74, 'gps_1')
    p2 = cogo.Point(153.98, 199.66, 'gps_2')

    print(p1, '\t', p2)
    print(cogo.distancia(p1, p2))


if __name__ == "__main__":
    main()
