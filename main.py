# Entry script for the dog reviews the mailman competition.
# Outputs a 1-star humorous review to stdout and target entry files.
import os
from pathlib import Path

ENTRY_LINE: str = (
    "1 star: Invades my territory daily smelling of ten rival dogs, shoves inedible paper into the door slot, and flees my ferocious bark before I can even roll over for belly rubs."
)


def build_line() -> str:
    return ENTRY_LINE


def main() -> None:
    # Ensure the entry file receives exactly one line with no extra whitespace.
    line = build_line()
    # Print exactly one funny line to stdout
    print(line)

    # Write line to local output/entry.txt for local verification
    repo_output_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    repo_output_path.parent.mkdir(parents=True, exist_ok=True)
    repo_output_path.write_text(f"{line}\n", encoding="utf-8")

    # Write line to container / environment output path if accessible
    env_target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    target_path = Path(env_target)
    if (
        target_path.is_dir()
        or env_target.endswith(("/", "\\"))
        or (not target_path.suffix and target_path.name != "entry.txt")
    ):
        target_path = target_path / "entry.txt"
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(f"{line}\n", encoding="utf-8")
    except Exception:
        pass


if __name__ == "__main__":
    main()
