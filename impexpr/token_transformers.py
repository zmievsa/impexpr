import re
import tokenize
from collections import deque, namedtuple
from io import StringIO
from typing import Any, Generator, List, Tuple


def modify_tokens(tokens: List[tokenize.TokenInfo]) -> Generator[Tuple[int, str], None, None]:
    imp_expr_started = False
    ignore_next_tkn = True
    current_import_elems = deque()
    for tkn1, tkn2 in zip(tokens, tokens[1:]):
        if imp_expr_started:
            if tkn1.string == ")":
                imp_expr_started = False
                import_expr = f'importlib.import_module("{".".join(current_import_elems)}")'
                yield from (t[:2] for t in tokenize.generate_tokens(StringIO(import_expr).readline))
                current_import_elems.clear()
            elif ignore_next_tkn:
                ignore_next_tkn = False
            elif tkn1.string != ".":
                current_import_elems.append(tkn1.string)

        elif tkn1.string == "(" and tkn2.string == "import":
            imp_expr_started = True
            ignore_next_tkn = True
        else:
            yield tkn1[:2]
    yield tokens[-1][:2]


def transform_source(source: str, **kwargs: Any) -> str:
    tokens = list(tokenize.generate_tokens(StringIO(source).readline))
    tokens = list(modify_tokens(tokens))
    source = tokenize.untokenize(tokens)
    return source


from rich import print

source = """
import importlib
for x in (import itertools).chain([1, 2], [3, 4], [5, 6]):
    print(x)
"""
exec(transform_source(source))
# print(list(tokenize.generate_tokens(StringIO(source).readline)))
