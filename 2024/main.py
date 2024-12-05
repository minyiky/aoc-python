"""Advent of Code: {{cookiecutter.year}} - Run All The Things."""

from __future__ import annotations

import argparse
import ast
import contextlib
import importlib
import inspect
import os
import sys
import time
from collections.abc import Generator
from typing import Any, Callable

import psutil

from rich.console import Console
from rich.table import Table
from rich_argparse import RichHelpFormatter


def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aoc-python",
        description="Advent of Code: 2024 (@minyiky)",
        epilog="Ho Ho Ho!",
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument(
        "days",
        type=str,
        default="all",
        nargs="?",
        help="The days to execute, split by commas (default: all)",
    )
    parser.add_argument(
        "--redact",
        default=False,
        action="store_true",
        help="Redact the solution values.",
    )
    parser.add_argument(
        "--example", default=False, action="store_true", help="Use example inputs."
    )
    return parser


@contextlib.contextmanager
def timer() -> Generator[Callable[[], tuple[Any, Any]]]:
    """Capture an inner block's execution time in nanoseconds, and cpu time."""
    # Initialize cpu counters
    cpu = psutil.cpu_times_percent()
    t1 = t2 = time.perf_counter_ns()

    def _timer() -> tuple[Any, Any]:
        t = t2 - t1
        return t, cpu

    yield _timer
    t2 = time.perf_counter_ns()
    cpu = psutil.cpu_times_percent()


def ns_to_ms(ns: float | int) -> float:
    """Convert nanoseconds to seconds."""
    return round(ns / 1000000.0, 6)


def yes_no(value: bool) -> str:
    """Convert boolean to a yes/no."""
    return "yes" if value else "no"


def format_cpu(cpu: Any) -> str:
    return f"user {cpu.user}%, sys {cpu.system}%"


def maybe_redact(value: str, redact: bool) -> str:
    """Maybe redact a value if asked to."""
    return "[dim grey]<redact>[/dim grey]" if redact else value


def purify_source(source: str) -> str:
    """Strip comments and other unneeded parts from source code."""
    return ast.unparse(ast.parse(source))


def run() -> None:
    parser = generate_parser()
    args = parser.parse_args(sys.argv[1:])

    days = [
        f"{s:02d}"
        for s in (range(1, 26) if args.days == "all" else args.days.split(","))
    ]

    # Import all modules and read all inputs, upfront
    modules = {}
    inputs = {}
    for day in days:
        with contextlib.suppress(ImportError):

            modules[day] = importlib.import_module(f".day{day}.solution", __package__)
            dir_path = os.path.dirname(os.path.realpath(__file__))

            with open(f"{dir_path}/day{day}/input.txt", "r") as f:
                input_data = f.read()

            inputs[day] = input_data

    table = Table(
        title="Advent of Code: 2024 (@minyiky)",
        row_styles=["", "dim"],
    )
    table.add_column("day", justify="right", style="bold cyan", no_wrap=True)
    table.add_column("p1", style="magenta")
    table.add_column("p2", style="green")
    table.add_column("cpu", justify="left", style="red")
    table.add_column("sloc (chr)", justify="right", style="yellow")
    table.add_column("t (seconds)", justify="right", style="blue")
    table.add_column("gold (t<1)", justify="right", style="gold3")

    total_seconds = 0.0
    for day, module in modules.items():
        with timer() as t_1:
            p1 = module.part_one(inputs[day])
        with timer() as t_2:
            p2 = module.part_two(inputs[day])
        if p1 == 0 and p2 == 0 and args.days == "all":
            # Ignore uncompleted days, unless explicitly mentioned
            continue
        t1, cpu = t_1()
        t2, _ = t_2()
        part_one_seconds = ns_to_ms(t1)
        part_two_seconds = ns_to_ms(t2)
        day_seconds = part_one_seconds + part_two_seconds
        total_seconds += day_seconds
        source = purify_source(inspect.getsource(module))
        sloc = source.count("\n")
        chars = len(source)
        table.add_row(
            day,
            str(maybe_redact(p1, args.redact)),
            str(maybe_redact(p2, args.redact)),
            format_cpu(cpu),
            f"{sloc} ({chars})",
            f"{day_seconds:.2f} ({part_one_seconds:.2f}, {part_two_seconds:.2f})".ljust(
                8, "0"
            ),
            yes_no(day_seconds < 1),
        )

    table.add_row(
        "total",
        "",
        "",
        "",
        "",
        f"{total_seconds:.6f}".ljust(8, "0"),
        yes_no(total_seconds < 1),
    )

    console = Console()
    console.print(table)


if __name__ == "__main__":  # pragma: no cover
    run()
