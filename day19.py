rules = {}
med = ''
with open('input19.txt') as f:
    data = f.read().split('\n\n')
    for line in data[0].splitlines():
        k, v = line.split(' => ', maxsplit=1)
        if k in rules:
            rules[k].append(v)
        else:
            rules[k] = [v]
    med = data[1].strip()

# Part 1
mut = set()
for k, v in rules.items():
    i = med.find(k)
    while i != -1:
        j = i + len(k)
        for r in v:
            mut.add(''.join((med[:i], r, med[j:])))
        i = med.find(k, j)
print(len(mut))

# Part 2
# This is not right, set becomes too big:
# 1 3
# 2 18
# 3 105
# 4 607
# 5 3566
# 6 21287
# 7 129071
# 8 793306
# 9 4933735
# Hints: https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
step = 0
mut = set('e')
while med not in mut:
    nxt = set()
    for mol in mut:
        for k, v in rules.items():
            i = mol.find(k)
            while i != -1:
                j = i + len(k)
                for r in v:
                    nxt.add(''.join((mol[:i], r, mol[j:])))
                i = mol.find(k, j)
    mut = nxt
    step += 1
    print(step, len(mut))
