rules = {}
rev = {}
med = ''
with open('input19.txt') as f:
    data = f.read().split('\n\n')
    for line in data[0].splitlines():
        k, v = line.split(' => ', maxsplit=1)
        if k in rules:
            rules[k].append(v)
        else:
            rules[k] = [v]
        rev[v] = k
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
print(sorted(rev.keys(), key=len, reverse=True))
