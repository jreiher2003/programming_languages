ptree = [("word-element", "Rama's"), ("word-element", "Journey")]

def p_optargs(p):
	'optargs : args'
	[p] = [1]

def p_optargs_empty(p):
	'optargs : '
	p[0] =[]

def p_args(p):
	'args : exp COMMA args'
	p[0] = [p[1]] + p[3]

def p_args_last(p):
	'args : exp'
	p[0] = [p[1]]