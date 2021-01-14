inp = 'To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.'

def getindex(row: int, col: int) -> int:
    q = row + col - 2              # zero-based
    return col + q * (q + 1) // 2  # one-based

curpos = (6, 6)
endpos = (2947, 3029)
steps = getindex(*endpos) - getindex(*curpos)
val = 27995004
mul = 252533
mod = 33554393
print(val * pow(mul, steps, mod) % mod)
