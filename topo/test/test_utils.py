import topo.cogo as cogo


def test_punto() -> None:
    A1 = cogo.Point2D(100, 200, 'cam')
    assert cogo.Point2D(100, 200, 'cam') == A1
    return


def test_gms() -> None:
    assert cogo.gms(39.50) == '39-30-00'
    return


def test_distancia() -> None:
    p1 = cogo.Point2D(240, 130)
    p2 = cogo.Point2D(200, 123.26)
    assert round(cogo.distancia(p2, p1), 4) == 40.564
    return
    