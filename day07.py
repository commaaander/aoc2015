import re
regrule = re.compile(r'^(([a-z0-9]+) )?(([A-Z]+) )?([a-z0-9]+) -> ([a-z]+)\n$')

func = {
    'AND'   : lambda x, y: x & y,
    'OR'    : lambda x, y: x | y,
    'NOT'   : lambda x: ~x,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'PATCH' : lambda x: x}

rules = []
with open('input07.txt') as f:
    for line in f:
        m = regrule.match(line)
        if m:
            id = m.group(4) if m.group(4) is not None else 'PATCH'
            inp = [int(x) if x.isnumeric() else x for x in m.group(2, 5) if x is not None]
            out = m.group(6)
            rules.append({'id': id, 'inp': inp, 'out': out, 'todo': True})

val = {}
while 'a' not in val:
    for i in range(len(rules)):
        if rules[i]['todo']:
            todo = False
            for j in range(len(rules[i]['inp'])):
                if type(rules[i]['inp'][j]) == str:
                    k = val.get(rules[i]['inp'][j])
                    if k is None:
                        todo = True
                    else:
                        rules[i]['inp'][j] = k
            if not todo:
                val[rules[i]['out']] = func[rules[i]['id']](*rules[i]['inp'])
                rules[i]['todo'] = False
print(val['a'])

val = {'b': 46065}
#TODO
print(val['a'])
