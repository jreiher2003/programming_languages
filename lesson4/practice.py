chart = { }
def csuffix(X,Y):
	if (X,Y) in chart:
		return chart[(X,Y)]
	else:
		answer = 0
		if X != "" and Y != "" and X[-1:] == Y[-1:]:
			answer = 1 + csuffix(X[:-1],Y[:-1])
		chart[(X,Y)] = answer
		return answer

print csuffix('Jeff', 'Beff')

def prefixes(X):
	return [X[:i+1] for i in range(len(X))]
print prefixes('Cat')
