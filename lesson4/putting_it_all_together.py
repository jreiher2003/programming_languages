grammar = [("S", ["P"]), ("P", ["(", "P", ")"]), ("P", []),]
tokens = ["(", "(", ")", ")"]

def addtochart(theset, index, elt):
	if not(elt in theset[index]):
		theset[index] = [elt] + theset[index]
		return True
	return False

def closure(grammar, i,x,ab,cd,j):
	next_states = [ (rule[0], [], rule[1],i) for rule in grammar if cd != [] and cd[0] == rule[0]]
	return next_states

def shift(tokens, i, x, ab, cd, j):
	if cd != [] and tokens[i] == cd[0]:
		return (x,ab + [cd[0]], cd[1:], j)
	else:
		return None

def reductions(chart, i ,x, ab, cd, j):
	return [(jstate[0], jstate[1] + [x], (jstate[2])[1:], jstate[3]) for jstate in chart[j] if cd==[] and jstate[2] <>[] and (jstate[2])[0] == x]

def parse(tokens, grammar):
	tokens = tokens + ["end_of_input_marker"]
	chart = {}
	start_rule = grammar[0]
	for i in range(len(tokens)+1):
		chart[i] = []
	start_state = (start_rule[0], [], start_rule[1], 0)
	chart[0] = [start_state]
	for i in range(len(tokens)):
		while True:
			changes = False
			for state in chart[i]
			x = state[0]
			ab = state[1]
			cd = state[2]
			j = state[3]
			next_states = closure(grammar,i,x,ab,cd,j)
			for next_state in next_states:
				changes = addtochart(chart,i,next_states) or changes

			next_state = shift(tokens,i,x,ab,cd,j)
			if next_state <> None:
				any_changes = addtochart(chart, i+1, next_state) or any_changes

			next_states = reductions(chart,i,x,ab,cd,j)
			for next_state in next_states:
				changes = addtochart(chart,i,next_state) or changes

		if not changes:
			break

	# #debugging
	# for i in range(len(tokens)):
	# 	print "== chart " + str(i)
	# 	for state in chart[i]:
	# 		x = state[0]

		accepting_state = (start_rule[0], start_rule[1], [], 0)
		return accepting_state in chart[len(tokens)-1]
		
	result = parse(tokens, grammar)