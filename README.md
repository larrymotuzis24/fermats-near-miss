# Looking for Fermat’s Last Theorem Near Misses

## What this program does
Prompts the user for n (3–11) and k (≥10), iterates all x,y in [10..k] to find the smallest
relative “near miss” to x^n + y^n = z^n. Prints each new smallest miss found and at the end
prints the overall best result with labeled values (x, y, z, S, miss, relative miss).

## Requirements
- Python 3.10+
- External libraries: none

## How to run (Python)
```bash
# macOS/Linux
python3 src/main.py
# Windows
py src\main.py
