import re
instr = re.compile(r'^(?P<op>[c-t]{3}) (?P<reg>a|b)?(?:, )?(?P<off>(?:\+|-)\d+)?$')

mem = []
with open('input23.txt') as f:
    for line in f:
        if m := instr.match(line.strip()):
            mem.append(m.groupdict())
            if mem[-1]['off'] is not None:
                mem[-1]['off'] = int(mem[-1]['off']) - 1

def run(a):
    reg = {'a': a, 'b': 0}
    ip = 0
    while ip >= 0 and ip < len(mem):
        i, r, j = mem[ip].values()
        if i == 'inc':
            reg[r] += 1
        elif i == 'hlf':
            reg[r] //= 2
        elif i == 'tpl':
            reg[r] *= 3
        elif i == 'jmp' or (i == 'jie' and reg[r] % 2 == 0) or (i == 'jio' and reg[r] == 1):
            ip += j
        ip += 1
    return reg['b']

print(run(0), run(1))
