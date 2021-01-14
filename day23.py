import re
instr = re.compile(r'^(?P<op>[c-t]{3}) (?P<reg>a|b)?(?:, )?(?P<off>(?:\+|-)\d+)?$')

mem = []
with open('input23.txt') as f:
    for line in f:
        if m := instr.match(line.strip()):
            mem.append(m.groupdict())
            if mem[-1]['off'] is not None:
                mem[-1]['off'] = int(mem[-1]['off'])

def run(a):
    reg = {'a': a, 'b': 0}
    ip = 0
    while ip >= 0 and ip < len(mem):
        a = mem[ip]
        if a['op'] == 'inc':
            reg[a['reg']] += 1
            ip += 1
        elif a['op'] == 'hlf':
            reg[a['reg']] //= 2
            ip += 1
        elif a['op'] == 'tpl':
            reg[a['reg']] *= 3
            ip += 1
        elif a['op'] == 'jmp':
            ip += a['off']
        elif a['op'] == 'jie':
            ip += a['off'] if reg[a['reg']] % 2 == 0 else 1
        elif a['op'] == 'jio':
            ip += a['off'] if reg[a['reg']] == 1 else 1
    return reg['b']

print(run(0), run(1))
