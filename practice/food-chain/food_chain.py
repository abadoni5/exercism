"""
This script generates verses of the song "I Know an Old Lady Who Swallowed a Fly"
based on a specified range of verses. It defines a function `recite` that takes
`start_verse` and `end_verse` parameters to determine which verses to generate.

Approach:
- Define constants:
  - `ANIMAL_LINES`: Contains tuples of animals and their associated phrases.
  - `SPIDER_LONG`: The extended phrase for the spider.
  - `FIRST_LINE`: The beginning of each verse.
- Define utility functions:
  - `she_swallowed`: Constructs the line describing the swallowing of one animal to catch another.
- Generate the verses:
  - Iterate over the animals and their phrases.
  - For each verse, construct the lines:
    - For the first verse, use the initial phrase and the animal's line.
    - For the second verse, add the phrase about the spider.
    - For the last verse, use only the animal's line.
    - For other verses, construct the line describing the swallowing of the current animal to catch the previous one.
  - Store the verses in a dictionary indexed by verse number.
- Recite the requested verses:
  - Concatenate the lines of the requested verses into a list.
  - Return the list of verses with empty strings between verses.
"""
from typing import List

ANIMAL_LINES = [
    ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!"),
]
SPIDER_LONG = "spider that wriggled and jiggled and tickled inside her"
FIRST_LINE = "I know an old lady who swallowed a "


def she_swallowed(curr_animal: str, prev_animal: str) -> str:
    return f"She swallowed the {curr_animal} to catch the {prev_animal}."


def recite(start_verse: int, end_verse: int) -> List[str]:
    verses = {}
    cumulative_verse = []
    prev_animal = ""

    for verse_num, line in enumerate(ANIMAL_LINES):
        curr_animal = line[0]
        animal_phrase = line[1]
        first_line = f"{FIRST_LINE}{curr_animal}."
        second_line = f"{animal_phrase}"
        if verse_num == 0:
            verses[verse_num] = [first_line, second_line]
            prev_animal = curr_animal
            cumulative_verse += [second_line]
        elif verse_num == 2:
            cumulative_verse = [
                she_swallowed(curr_animal, SPIDER_LONG)
            ] + cumulative_verse
            verse = [first_line, second_line] + cumulative_verse
            verses[verse_num] = verse
        elif verse_num == 7:
            verses[verse_num] = [first_line, second_line]
        else:
            cumulative_verse = [
                she_swallowed(curr_animal, prev_animal)
            ] + cumulative_verse
            verse = [first_line, second_line] + cumulative_verse
            verses[verse_num] = verse
        prev_animal = curr_animal

    recited = []
    for verse_num in range(start_verse, end_verse + 1):
        recited += verses[verse_num - 1]
        if verse_num < end_verse:
            recited.append("")
    return recited
