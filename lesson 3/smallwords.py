lst = []
"""
def smallwords(lst):
	yield [x for x in lst if len(x)> 3]
"""
def smallwords(lst):
	for x in lst:
		if len(x) <= 3:
			yield x

print [x for x in smallwords(lst)] 
print [x for x in lst if len(x) > 3]


def expand(tokens, grammar):
	for pos in range(len(tokens)):
		for rule in grammar:
			if tokens[pos] == rule[0]:
				yield tokens[0:pos] + rule[1] + tokens[pos+1:]