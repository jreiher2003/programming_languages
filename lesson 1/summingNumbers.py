import re

def sumnums(sentence):
	r = r"[0-9]+"
	sum1 = 0
	for found in re.findall(r,sentence):
		sum1 += int(found)
	return sum1