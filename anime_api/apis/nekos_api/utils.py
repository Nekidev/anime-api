"""
Utilities to make easier the implementation of the wrapper.
"""


class EscapedQuery:
    """
    Escapes a search query.
    """

    def __init__(self, query: str):
        self.query = query

    def escaped_query(self) -> str:
        """
        Escapes special characters
        """
        mapping = {}
        special_characters = [
            "%",
            "_",
            "|",
            "*",
            "+",
            "?",
            "{",
            "}",
            "(",
            ")",
            "[",
            "]",
        ]

        for character in special_characters:
            mapping.update({character: f"\\{character}"})

        table = str.maketrans(mapping)
        return self.query.translate(table)

    def __str__(self):
        """
        Returns escaped query.
        """
        return self.escaped_query()
