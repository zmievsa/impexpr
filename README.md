# Impexpr
A simple superset of Python with import expressions added in. Beware: This project has only been made as a proof of concept and is not intended to ever be used in production. 

## Installation
```bash
pip install impexpr
```
## Quickstart
* If you wish to import itertools and use it in the same line, run `impexpr` with the file with the following contents as the first argument:
```python
for x in (import itertools).chain([1, 2], [3, 4], [5, 6]):
    print(x)
```
* For everything else, run `impexpr --help`