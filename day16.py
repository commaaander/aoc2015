id = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
sue = []
with open('input16.txt') as f:
    for line in f:
        _, has = line.strip().split(': ', maxsplit=1)
        has = has.split(', ')
        d = {}
        for h in has:
            k, v = h.split(': ', maxsplit=1)
            d[k] = int(v)
        sue.append(d)

# Part 1
sel0 = set(range(len(sue)))
sel1 = sel0.copy()
for k, v in id.items():
    for i in sel0:
        if k in sue[i]:
            if sue[i][k] != v:
                sel1.remove(i)
    sel0 = sel1.copy()
print(sel0.pop() + 1)

# Part 2
sel0 = set(range(len(sue)))
sel1 = sel0.copy()
for k, v in id.items():
    for i in sel0:
        if k in sue[i]:
            if k == 'cats' or k == 'trees':
                # must be greater
                if sue[i][k] <= v:
                    sel1.remove(i)
            elif k == 'pomeranians' or k == 'goldfish':
                # must be fewer than
                if sue[i][k] >= v:
                    sel1.remove(i)
            else:
                if sue[i][k] != v:
                    sel1.remove(i)
    sel0 = sel1.copy()
print(sel0.pop() + 1)
