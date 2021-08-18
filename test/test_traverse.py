from operations import _traverse


def test_empty():
    matrix = []
    answer = []
    assert _traverse(matrix) == answer


def test_one():
    matrix = [[10]]
    answer = [10]
    assert _traverse(matrix) == answer


def test_two():
    matrix = [
        [10, 20],
        [30, 40],
    ]
    answer = [
        10, 30,
        40, 20,
    ]
    assert _traverse(matrix) == answer


def test_three():
    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ]
    answer = [
        10, 40, 70,
        80, 90, 60,
        30, 20, 50,
    ]
    assert _traverse(matrix) == answer


def test_four():
    matrix = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]
    answer = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]
    assert _traverse(matrix) == answer


def test_five():
    matrix = [
        [10,  20,  30,  40,  50],
        [60,  70,  80,  90,  100],
        [110, 120, 130, 140, 150],
        [160, 170, 180, 190, 200],
        [210, 220, 230, 240, 250],
    ]
    answer = [
        10, 60, 110, 160, 210,
        220, 230, 240, 250, 200,
        150, 100, 50, 40, 30,
        20, 70, 120, 170, 180,
        190, 140, 90, 80, 130,
    ]
    assert _traverse(matrix) == answer
