# Matrix

This small package provides a function get_matrix, which retrieves a square matrix (NxN) from a remote server, traverses it in a spiral, starting from the upper-left corner, and returns it to the user as a List[int].

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matrix.

```bash
pip install https://github.com/alexey1214/matrix/raw/master/dist/matrix-0.0.1.tar.gz
```

## Usage

```python
>>> import asyncio
>>> from matrix import get_matrix
>>>
>>> url = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'
>>> asyncio.run(get_matrix(url))
[10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
>>>
```

## License

[MIT](https://choosealicense.com/licenses/mit/)