import os
import sys

from aocd.models import default_user
from aocd.types import PuzzlePart, PuzzleStats

from ..parser import parse_examples
from .formatting import _format_day, _format_path

# The path to your README file
readme_filename = "README.md"


# Function to get stars for a specific day using aocd
def get_stars_for_day(
    stats: dict[str, dict[PuzzlePart, PuzzleStats]], year: int, day: int
):
    result = stats[f"{year}/{day:02d}"]
    return "⭐" * len(result)  # Return stars based on how many parts are completed


# Function to get the title for a specific day using aocd
def get_day_title(year: int, day: int):
    """
    Gets the title for the day specified by day_number.

    This function will attempt to read the example.txt file for the day specified
    by day_number and parse the title from it.

    Args:
        day_number (int): The day number for which to get the title.

    Returns:
        str: The title for the specified day.
    """
    example_path = os.path.join(_format_path(year, day), "example.txt")

    if not os.path.exists(example_path):
        print(f"file not found here: {example_path}")
        raise FileNotFoundError(f"Example file not found for day {day}")

    with open(example_path, "r") as f:
        example_content = f.read()

    title, _ = parse_examples(example_content)
    return title


# A function to generate the day rows for the README
def generate_day_rows(year: int, stats, days_info: list[str]):
    """
    Generates a list of rows for the README table containing the days.

    Args:
        year (int): The year for which to generate the table.
        stats (dict): A dictionary containing the stats for the year, as returned
            by `aocd.User.get_stats`.
        days_info (list[str]): A list of strings already populated day information.

    Returns:
        list[str]: A list of strings, each representing a row in the table.
    """
    day_rows = []

    for day in range(1, 26):
        try:
            # Get the actual title for the day
            day_title = get_day_title(year, day)

            # Get the stars for the day from AoC
            stars = get_stars_for_day(stats, year, day)

            notes = ""
            try:
                day_info = days_info[day]
                notes = day_info.split("|")[-2].strip()
            except IndexError:
                pass

            # Build the row for the table
            day_rows.append(
                f"| Day {day}: {day_title} |  {stars}  | [python]({_format_day(day)}/) | {notes} |"
            )
        except FileNotFoundError:
            break

    return day_rows


# Function to read the current README file and update only the table lines
def update_readme(year: int):
    try:
        user = default_user()
        # Fetch the stars for the current day using aocd
        try:
            # Attempt to get data for both parts of the day
            stats = user.get_stats(2024)
        except Exception:
            pass  # If part is not completed, skip it
    except Exception:
        return

    readme_path = f"{year}/{readme_filename}"

    with open(readme_path, "r") as file:
        readme_content = file.readlines()

    print()

    # Find the header and the table section
    table_start_idx = None
    table_end_idx = None
    days_info = []
    for i, line in enumerate(readme_content):
        if line.startswith("| ---"):
            table_start_idx = i

        if table_start_idx is not None:
            if not line.startswith("|"):
                table_end_idx = i
                break
            days_info.append(line.strip())

    # If the table was found, replace only the rows
    if table_start_idx is not None and table_end_idx is not None:
        # Get the updated table rows
        day_rows = generate_day_rows(year, stats, days_info)

        # Replace the old table rows with the new ones
        new_readme_content = readme_content[
            : table_start_idx + 1
        ]  # Keep the header intact
        new_readme_content.append("\n".join(day_rows) + "\n")  # Append the new rows
        new_readme_content.extend(
            readme_content[table_end_idx:]
        )  # Keep the header intact
        new_readme_content.append(
            ""
        )  # Ensure we end with an empty line after the table

    # Write the updated content back to the README file
    with open(readme_path, "w") as file:
        file.writelines(new_readme_content)


def main():
    if len(sys.argv) < 2:
        print("Please specify the year (e.g., python generate_files.py 2024)")
        sys.exit(1)

    year = int(sys.argv[1])
    update_readme(year)
    print(f"Template files generated for year {year}")


if __name__ == "__main__":
    main()
