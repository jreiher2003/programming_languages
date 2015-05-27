"""from intertools import chain, combinations
def powerset(iterable):
	xs = list(iterable)
	return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

print list(powerset(set([1,2,3,4,5])))"""

import itertools
stuff = [1, 2, 3, 4, 5]
for L in range(0, len(stuff)+1):
  for subset in itertools.combinations(stuff, L):
    print(subset)