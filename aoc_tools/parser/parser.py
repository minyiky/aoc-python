"""parse allows extracting data from the examples file generated by aocd"""

from dataclasses import dataclass
from typing import Tuple
import re


@dataclass
class ExampleData:
    example_number: int
    data: str
    answer_a: int
    answer_b: int


def parse_examples(file_content: str) -> Tuple[str, list[ExampleData]]:
    """parse reads all data from an examples file

    Args:
        filepath (str): The location of the example file
    """
    day_title = re.findall(r"--- Day (\d+): (.+?) ---", file_content)
    if day_title:
        _, title = day_title[0]
    else:
        raise ValueError("Day title not found.")

    # Find the day title and the input data
    examples: list[ExampleData] = []

    # Parse example data and answers
    example_sections = re.findall(
        r"""------------------------------- Example data (\d+)/(\d+) -------------------------------
(.*?)
--------------------------------------------------------------------------------
answer_a: (.*?)
answer_b: (.*?)
--------------------------------------------------------------------------------""",
        file_content,
        re.DOTALL,
    )

    for example_data in example_sections:
        example_number, _, data, answer_a, answer_b = example_data
        if answer_a == "-":
            answer_a = 0
        if answer_b == "-":
            answer_b = 0
        examples.append(
            ExampleData(
                example_number=int(example_number),
                data=data.strip(),
                answer_a=int(answer_a),
                answer_b=int(answer_b),
            )
        )

    return title, examples


def get_example_data(
    examples: list[ExampleData], example_number: int
) -> Tuple[str, int | None]:
    """get_example_data pulls out the relevant information from
    an example file for the part specified

    Args:
        examples (list[ExampleData]): _description_
        example_number (int): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    # Retrieve the example based on the given number
    if example_number == 1:
        # For test 1, always return answer_a from example 1
        e = examples[0]  # Always take the first example for test 1
        return e.data, e.answer_a
    elif example_number == 2 and len(examples) == 1:
        # If there is only a single example return answer_b from example 1
        e = examples[0]  # Always take the first example for test 1
        return e.data, e.answer_b
    elif example_number == 2 and len(examples) > 1:
        # If there is more than a single example return answer_a from example 2
        e = examples[1]  # Always take the second example for test 2
        return e.data, e.answer_a
    else:
        raise ValueError(f"Example {example_number} not found or doesn't exist.")
