import pytest

from matrix.operations import get_matrix


@pytest.mark.asyncio
async def test_correct():
    url = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'
    answer = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]
    assert await get_matrix(url) == answer
