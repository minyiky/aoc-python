# Advent of Code Solutions

This repository contains my solutions for the Advent of Code challenges, written in Python. Each year’s solutions will be organized in their respective folders.

For other languages that I have written solution for advent of code in see here:
 - [Golang](https://github.com/minyiky/advent-of-code)

## Project Structure

The repository is organized as follows:

- Each year's solutions are placed in a folder named after the year (e.g., `2024`).
- Inside the folder for each year, each day’s solution is contained in a subfolder named `dayXX`, where `XX` is the day number.
- Each day's folder includes:
  - `solution.py`: The Python script containing the solution for that day's challenge.
  - `example.txt`: Example input for testing.
  - `dayXX_test.py`: Unit tests for the solution (using Python's `unittest` or `pytest`).

*Note:* The input files are deliberately not included in the repository as [requested](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/).

Additionally, the project contains:
- `Makefile`: Used to automate workflows such as testing, building, and running solutions.
- `aoc_tools/`: A folder containing utility scripts.
- `requirements.txt`: Python dependencies required for running the solutions and tools.

## How to Set Up

### 1. Clone the repository:

```bash
git clone https://github.com/minyiky/aoc-python.git
cd aoc-python
```

### 2. Install the dependencies:

Use pip to install the necessary packages:
```bash
pip install -r requirements.txt
```

### 3. How to Use:

#### Run a Solution:
Each day’s solution is in its respective `YYYY/dayDD/solution.py` file. You can run any solution by executing the corresponding Python script, e.g.:

```bash
python 2024/day01/solution.py
```

You can also use the Makefile to by running:

```bash
make run [YEAR=YYYY] [DAY=D]
```

#### Testing:

Each day’s folder includes a test file (e.g., day01_test.py) for running unit tests. You can run the tests using e.g.:

```bash
python -m unittest 2024/day01/day01_test.py
```

Or run all tests for a year with:

```bash
python -m unittest discover 2024 "*test.py"
```

You can also use the Makefile to by running:

```bash
make test [YEAR=YYYY]
```


## License
This project is licensed under the MIT License - see the LICENSE file for details.