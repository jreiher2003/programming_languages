def addtochart(chart, index, state):
	if not state in chart[index]:
		chart[index]+=state
		return True
	else:
		return False