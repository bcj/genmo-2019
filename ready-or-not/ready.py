"""
Ready or Not—A hide-and-seek adventure
"""
from argparse import ArgumentParser
from pathlib import Path
from random import choice
from typing import Iterator, List, Optional

NOVEL_LENGTH = 50_000

NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}
NUMBER_GROUPS = ("thousand", "million", "billion", "trillion")
UNNAMED = 10 ** ((len(NUMBER_GROUPS) + 1) * 3)  # first unnamed number
SPACERS = (("one", "thousand"), ("Mississippi",), ("banana",))
COUNT_TO = 10_000  # NB, wc counts hyphenated words as 2 words.


def generate(path: Path, count_to: int = COUNT_TO) -> None:
    """
    Generate a novel.

    path: Where to save the novel to.
    """
    spacer_phrase = " ".join(("", *choice(SPACERS)))
    count_name = " ".join(number_name(count_to))

    with path.open("w") as stream:
        stream.write(f"Ready or Not\n\n\tAlright, I'm counting to {count_name}.")

        for pos, number in enumerate(count(count_to), 1):
            if pos < count_to:
                spacer = spacer_phrase
            else:
                spacer = ""
            stream.write(f" {' '.join(number).capitalize()}{spacer}.")

        stream.write(" Ready or not, here I come!")


def count(stop_at: Optional[int] = None) -> Iterator[List[str]]:
    """
    Count from one using words. Yields a list of words

    stop_at: If given, stop counting once this number is reached
    """
    counter = 1

    while stop_at is None or counter <= stop_at:
        yield number_name(counter)
        counter += 1


def number_name(number) -> List[str]:
    """
    Returns the list of words used to describe a number.
    """
    if number == 0:
        return ["zero"]

    words = []

    if number < 0:
        words.append("negative")
        number = -number

    if number >= UNNAMED:
        raise NotImplementedError(f"I don't know what {number} is called")

    digits = len(str(number))

    groups = max(0, digits + 2) // 3

    for group in range(groups, 0, -1):
        section = (number % (1000 ** group)) // (1000 ** (group - 1))

        hundreds = section // 100

        if hundreds:
            words.extend((NUMBERS[hundreds], "hundred"))

        tens_ones = section % 100

        word = NUMBERS.get(tens_ones, None)

        if word:
            words.append(word)
        else:
            ones = tens_ones % 10
            tens = tens_ones - ones

            if tens:
                if ones:
                    words.append(f"{NUMBERS[tens]}-{NUMBERS[ones]}")
                else:
                    words.append(NUMBERS[tens])
            elif ones:
                words.append(NUMBERS[ones])

        if group > 1 and section:
            words.append(NUMBER_GROUPS[group - 2])

    return words


def main():
    """
    Run ready-or-not from the command line.
    """
    parser = ArgumentParser(description="Generate a hide-and-seek adventure")
    parser.add_argument("path", type=Path, help="Where to write the novel to.")

    args = parser.parse_args()

    generate(args.path)


if __name__ == '__main__':
    main()
