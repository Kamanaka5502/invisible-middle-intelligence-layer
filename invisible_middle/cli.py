import json
import sys

from invisible_middle.classifier import classify
from invisible_middle.reports import generate_markdown_report


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python -m invisible_middle.cli <case.json>")
        raise SystemExit(1)

    path = sys.argv[1]

    with open(path, "r", encoding="utf-8") as f:
        case = json.load(f)

    interpretation = classify(case)

    report = generate_markdown_report(interpretation)

    print(report)


if __name__ == "__main__":
    main()
