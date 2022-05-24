# Impexpr
A simple superset of Python with import expressions added in. Beware: This project has only been made as a proof of concept and is not intended to ever be used in production. 

## Installation
```bash
pip install impexpr
```
## Quickstart
`impexpr` alias can be used in the same way as `python` alias, a few examples:
* To run an interactive REPL with import expression support, run `impexpr`
* To run a script, run `impexpr script.py` (all imported modules will also support import expressions) 
* To import itertools and use it in the same line:
```python
for x in (import itertools).chain([1, 2], [3, 4], [5, 6]):
    print(x)
```
* To get help about collections.deque:
```python
help((import collections).deque)
```
* If your script must run with python alias but you want to enable import expression support in all imported modules (not in the main script!), you can use:
```python
import impexpr
impexpr.add_hook()
# this will now support import expressions
import my_other_script
```
* For everything else, run `impexpr --help`

## FAQ
* Relative imports not supported yet 