# 2023 Advent of Code solutions

![](https://img.shields.io/badge/tests%20passed%20🐍-4/4-success)
![](https://img.shields.io/badge/day%20📅-2-blue)
![](https://img.shields.io/badge/stars%20⭐-4-yellow)
![](https://img.shields.io/badge/days%20completed-2-red)

Here are my results for the [2024 advent of code](https://adventofcode.com/2024) competition


| *Day* | *Stars* | *Solution* | *Notes* |
|-------|---------|------------|---------|
| Day 1: Historian Hysteria |  ⭐⭐  | [python](day01/) | A relatively strait forward day of splitting an input into ints and comparing lists |
| Day 2: Red-Nosed Reports |  ⭐⭐  | [python](day02/) | Part 2 was a little trickier to implement reasoned logic, but recursion saves the day |


## Running the code

*Note*: The following commands can be modified by running setting the `YEAR` and `DAY` variables.

To run the go code, you must be in this directory before running any of the following commands. You will also need to create `input.txt` files. To create an input for the current day run:

``` bash
make fetch-input
```

To run all solutions for the current year you can use:
```bash
make run
```

The run a single day (defaulting to today) use:
``` bash
make run-day
```

To run the tests use:
```bash
make test
```

To only test a single day (defaulting to today) use:
```bash
make test-day
```
