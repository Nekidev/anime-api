import re
import typing


def camel_to_snake(s) -> str:
    return re.sub("([A-Z]\w+$)", "_\\1", s).lower()


def to_snake(d) -> typing.Union[dict, list]:
    """
    Converts a dict or list to snake case from camel case
    """
    if isinstance(d, list):
        return [to_snake(i) if isinstance(i, (dict, list)) else i for i in d]
    return {
        camel_to_snake(a): to_snake(b) if isinstance(b, (dict, list)) else b
        for a, b in d.items()
    }
