# https://app.codesignal.com/arcade/code-arcade/intro-gates/bszFiQAog96G9CXKg

def seatsInTheater(cols: int, rows: int, col: int, row: int) -> int:
    return (cols - col + 1) * (rows - row)
