# sudoku-solver

Handy little code to resolve sudokus (yes, even the hard ones)

## How to
- run `sudoku_solver.py`
- enter your sudoku grid as a single line (starting from the upper left corner and moving right) with `0` instead of empty boxes. So for example, if your sudoku grid looks like this:
```python
- - - - - - - - - - - - - 
| 9 1   | 3   5 |       |
|     4 | 1     |   8 5 |
|   5   | 4   2 |   1   |
- - - - - - - - - - - - - 
|     8 |     1 |     4 |
| 4 2   |       | 1 6   |
| 1     | 6     | 5     |
- - - - - - - - - - - - - 
|       | 2   3 |   7   |
|   4   |     7 | 6     |
|       | 9   6 |   5 1 |
- - - - - - - - - - - - - 
```
just enter
```python
910305000004100085050402010008001004420000160100600500000203070040007600000906051
```
* tada!
