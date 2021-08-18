from operations import _parse


def test_empty():
    text = ''
    answer = []
    assert _parse(text) == answer


def test_one():
    text = '+-----+\n' \
           '|  10 |\n' \
           '+-----+'
    answer = [[10]]
    assert _parse(text) == answer


def test_four():
    text = '+-----+-----+-----+-----+\n' \
           '|  10 |  20 |  30 |  40 |\n' \
           '+-----+-----+-----+-----+\n' \
           '|  50 |  60 |  70 |  80 |\n' \
           '+-----+-----+-----+-----+\n' \
           '|  90 | 100 | 110 | 120 |\n' \
           '+-----+-----+-----+-----+\n' \
           '| 130 | 140 | 150 | 160 |\n' \
           '+-----+-----+-----+-----+'
    answer = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]
    assert _parse(text) == answer
