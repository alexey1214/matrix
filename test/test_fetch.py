import pytest

from aiohttp import ClientError

from operations import _fetch


@pytest.mark.asyncio
async def test_correct_response():
    url = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'
    answer = '+-----+-----+-----+-----+\n' \
             '|  10 |  20 |  30 |  40 |\n' \
             '+-----+-----+-----+-----+\n' \
             '|  50 |  60 |  70 |  80 |\n' \
             '+-----+-----+-----+-----+\n' \
             '|  90 | 100 | 110 | 120 |\n' \
             '+-----+-----+-----+-----+\n' \
             '| 130 | 140 | 150 | 160 |\n' \
             '+-----+-----+-----+-----+\n'
    text = await _fetch(url)
    assert text == answer


@pytest.mark.asyncio
async def test_invalid_url():
    with pytest.raises(ValueError, match=f'Invalid URL "*"'):
        url = 'invalid_url'
        await _fetch(url)


@pytest.mark.asyncio
async def test_client_error():
    with pytest.raises(ClientError):
        url = 'https://f00.backblazeb2.com/file/am-avito/matrix.txt'
        await _fetch(url)