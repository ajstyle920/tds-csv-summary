"""csv_summary.py - quick summary of any CSV file.

Usage:
    python csv_summary.py sample.csv
    python csv_summary.py sample.csv --top 3
"""
import argparse
import csv
import statistics
import sys


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames or [], rows


def summarise_column(name, values, top):
    filled = [v.strip() for v in values if v and v.strip()]
    missing = len(values) - len(filled)
    print(f"\n== {name} ==")
    print(f"  filled: {len(filled)}   missing: {missing}")
    if not filled:
        return
    if all(is_number(v) for v in filled):
        nums = [float(v) for v in filled]
        print("  type:   numeric")
        print(f"  min:    {min(nums):g}")
        print(f"  max:    {max(nums):g}")
        print(f"  mean:   {statistics.mean(nums):.2f}")
        print(f"  median: {statistics.median(nums):g}")
    else:
        counts = {}
        for v in filled:
            counts[v] = counts.get(v, 0) + 1
        common = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
        print("  type:   text")
        print(f"  unique: {len(counts)}")
        print("  most common: " + ", ".join(f"{k} ({c})" for k, c in common))


def main():
    parser = argparse.ArgumentParser(description="Summarise a CSV file.")
    parser.add_argument("path", help="path to a CSV file with a header row")
    parser.add_argument("--top", type=int, default=3,
                        help="how many common text values to show (default 3)")
    args = parser.parse_args()

    try:
        columns, rows = load_csv(args.path)
    except FileNotFoundError:
        sys.exit(f"File not found: {args.path}")

    if not columns:
        sys.exit("The file has no header row.")

    print(f"File: {args.path}")
    print(f"Rows: {len(rows)}   Columns: {len(columns)}")
    for name in columns:
        summarise_column(name, [row.get(name) or "" for row in rows], args.top)


if __name__ == "__main__":
    main()
