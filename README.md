# CSV Summary

A small Python command-line tool that gives a quick overview of any CSV file:
row and column counts, missing values, and simple stats for each column.

- **Numeric columns:** min, max, mean, median
- **Text columns:** number of unique values and the most common ones

No libraries to install. It uses only the Python standard library.

## How to run

```bash
python csv_summary.py sample.csv
python csv_summary.py sample.csv --top 5
```

## Example output

```
File: sample.csv
Rows: 8   Columns: 5

== city ==
  filled: 8   missing: 0
  type:   text
  unique: 4
  most common: Chennai (3), Delhi (2), Mumbai (2)

== score ==
  filled: 6   missing: 2
  type:   numeric
  min:    68
  max:    91
  mean:   80.33
  median: 80.5
```

## Files

| File | What it is |
|------|------------|
| `csv_summary.py` | The tool (under 100 lines) |
| `sample.csv` | Example data to try it on |
| `index.html` | Project page for GitHub Pages |

## Ideas for later

- Export the summary as JSON
- Detect date columns
- Show a simple text histogram for numeric columns
