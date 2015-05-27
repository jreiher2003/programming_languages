#a lexer is a collection of token definitions

def t_WHITESPACE(token):
	r' '
	pass

def t_WORD(token):
	r'[^ <>]+'
	return token

def t_NUMBER(token):
	r'[0-9]+'
	token.value = int(token.value)
	return token

