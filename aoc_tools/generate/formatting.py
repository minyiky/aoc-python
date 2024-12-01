def _format_day(day: int) -> str:
    return f"day{day:02d}"


def _format_path(year: int, day: int) -> str:
    """Format the path to the day folder."""
    return f"{year}/{_format_day(day)}"
