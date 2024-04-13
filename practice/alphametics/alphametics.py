from itertools import permutations
from typing import Dict, Optional, List, Tuple


def parse_puzzle(puzzle: str) -> Tuple[List, str]:
    """
    Parse the alphametics puzzle into a list of words and the result.

    Args:
        puzzle (str): The alphametics puzzle to parse.

    Returns:
        Tuple[List, str]: A tuple containing a list of words and the result.
    """
    inputs, value = puzzle.split(" == ")
    words = [i.strip() for i in inputs.split("+")]
    return (words, value.strip())


def solve(puzzle: str) -> Optional[Dict[str, int]]:
    """
    Solve an alphametics puzzle.

    Args:
        puzzle (str): The alphametics puzzle to solve.

    Returns:
        Optional[Dict[str, int]]: A dictionary mapping characters to digits if a solution is found,
                                  otherwise None.
    """
    words, value = parse_puzzle(puzzle)
    nonzero = set([w[0] for w in words + [value] if len(w) > 1])
    letters = list(set("".join(words + [value])) - nonzero) + list(nonzero)
    for perm in permutations("0123456789", len(letters)):
        conv_dict = dict(zip(letters, perm))
        if "0" in perm[-len(nonzero) :]:
            continue

        values = [int("".join(conv_dict[w] for w in word)) for word in words]
        summed = int("".join(conv_dict[v] for v in value))

        if sum(values) == summed:
            return {k: int(v) for k, v in conv_dict.items()}
    return None
