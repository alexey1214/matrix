import re

from typing import List

import aiohttp

from aiohttp import InvalidURL, ClientError


async def _fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:  # TODO: Reuse session
        try:
            async with session.get(url) as response:
                return await response.text()
        except InvalidURL:
            raise ValueError(f'Invalid URL "{url}"')
        except ClientError:
            raise


def _parse(text: str) -> List[List[int]]:
    matrix = []
    re_numbers = re.compile(r'\d+')

    for line in text.split('\n'):
        if line.startswith('|'):
            numbers = re_numbers.findall(line)
            matrix.append([int(n) for n in numbers])

    return matrix


def _traverse(matrix: List[List[int]]) -> List[int]:
    traversal = []
    size = len(matrix)

    for loop in range(size // 2 + size % 2):

        for i in range(0 + loop, size - loop):
            elem = matrix[i][0 + loop]
            traversal.append(elem)

        for j in range((0 + loop) + 1, size - loop):
            elem = matrix[(size - 1) - loop][j]
            traversal.append(elem)

        for i in range((size - 1) - loop - 1, 0 + loop - 1, -1):
            elem = matrix[i][(size - 1) - loop]
            traversal.append(elem)

        for j in range((size - 1) - loop - 1, 0 + loop, -1):
            elem = matrix[(0 + loop)][j]
            traversal.append(elem)

    return traversal


async def get_matrix(url: str) -> List[int]:
    try:
        text = await _fetch(url)
    except Exception:
        raise
    matrix = _parse(text)
    return _traverse(matrix)