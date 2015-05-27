def t_IDENTIFIER(token):
	r'[a-zA-Z]+_*[a-zA-Z]+'
	return token

def t_NUMBER(token):
	r'-?[0-9]+[\.]?[0-9]*'
	token.value = float(token.value)
	return token

#end of the line rule of js
def t_eolcomment(token):
	r'//[^\n]*'
	pass