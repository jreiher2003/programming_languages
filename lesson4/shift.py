def shift(tokens, i, x, ab, cd, j):
	#x->ab *cd for i tokens[i] ==c?
	if cd <> [] and tokens[i] == cd[0]:
		return (x, ab + [cd[0]], cd[1:], j)
	else:
		return None

def reductions(chart, i ,x, ab, cd, j):
	return [(jstate[0], jstate[1] + [x], (jstate[2])[1:], jstate[3]) for jstate in chart[j] if cd==[] and jstate[2] <>[] and (jstate[2])[0] == x]