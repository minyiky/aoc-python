# 2024 Advent of Code solutions

![](https://img.shields.io/badge/tests%20passed%20🐍-40/40-success)
![](https://img.shields.io/badge/stars%20⭐-40-yellow)
![](https://img.shields.io/badge/days%20completed-20-red)

Here are my results for the [2024 advent of code](https://adventofcode.com/2024) competition

| _Day_                          | _Stars_ | _Solution_       | _Notes_                                                                                                                  |
| ------------------------------ | ------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Day 1: Historian Hysteria      | ⭐⭐    | [python](day01/) | A relatively strait forward day of splitting an input into ints and comparing lists                                      |
| Day 2: Red-Nosed Reports       | ⭐⭐    | [python](day02/) | Part 2 was a little trickier to implement reasoned logic, but recursion saves the day                                    |
| Day 3: Mull It Over            | ⭐⭐    | [python](day03/) | A bit of regex today, some care is needed with how the input is formatted though                                         |
| Day 4: Ceres Search            | ⭐⭐    | [python](day04/) | Python automatically handling negative list indexes was the biggest debugging issue for this day                         |
| Day 5: Print Queue             | ⭐⭐    | [python](day05/) | Bubble bubble                                                                                                            |
| Day 6: Guard Gallivant         | ⭐⭐    | [python](day06/) | A traditional path following puzzle today, brute forcing is quick enough but there are definitely improvements to be had |
| Day 7: Bridge Repair           | ⭐⭐    | [python](day07/) | Another day where recursion and caching allowed for intelligent traversal of the tree                                    |
| Day 8: Resonant Collinearity   | ⭐⭐    | [python](day08/) | Take a close look at the input, it makes this day much simpler                                                           |
| Day 9: Disk Fragmenter         | ⭐⭐    | [python](day09/) | The inputs held a tricky situation today and remember,. numbers can have more than one digit                             |
| Day 10: Hoof It                | ⭐⭐    | [python](day10/) | Turns out reading the question is useful, but I was not alone, BFS was the route in this one                             |
| Day 11: Plutonian Pebbles      | ⭐⭐    | [python](day11/) | All about recursion,lists are definitely not the way                                                                     |
| Day 12: Garden Groups          | ⭐⭐    | [python](day12/) | A slightly more complex day solved by thinking carefully about how to determine constant edges                           |
| Day 13: Claw Contraption       | ⭐⭐    | [python](day13/) | Maths wins today                                                                                                         |
| Day 14: Restroom Redoubt       | ⭐⭐    | [python](day14/) | Lots of _ways_ to solve this one, mine was based on a lucky assumption                                                   |
| Day 15: Warehouse Woes         | ⭐⭐    | [python](day15/) | A grid based block moving task, many ways to solve this, and very easy in som physics based engines                      |
| Day 16: Reindeer Maze          | ⭐⭐    | [python](day16/) | Another grid based task today, nothing too special in this one                                                           |
| Day 17: Chronospatial Computer | ⭐⭐    | [python](day17/) | A fun "intcode" style problem toady where careful inspection of the input gave all the clues needed for this             |
| Day 18: RAM Run                | ⭐⭐    | [python](day18/) | More grids this time, lots of branching in this one                                                                      |
| Day 19: Linen Layout           | ⭐⭐    | [python](day19/) | Looked harder than it was, memoisation came in key today                                                                 |
| Day 20: Race Condition         | ⭐⭐    | [python](day20/) | More Grids (Sesing a theme here), still more opimisation possible here as there is lots of speed to be improved          |

## Running the code

_Note_: The following commands can be modified by running setting the `YEAR` and `DAY` variables.

To run the go code, you must be in this directory before running any of the following commands. You will also need to create `input.txt` files. To create an input for the current day run:

```bash
make fetch-input
```

To run all solutions for the current year you can use:

```bash
make run
```

The run a single day (defaulting to today) use:

```bash
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
