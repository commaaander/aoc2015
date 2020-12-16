import re

func = {
    'AND'   : lambda x, y: x & y,
    'OR'    : lambda x, y: x | y,
    'NOT'   : lambda x: ~x,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y}
rule = {}

with open('input07.txt') as f:
