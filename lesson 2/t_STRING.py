def t_STRING(token):
	r'"[^"]*"'
	token.value = tokenvalue[1:-1]
	return token
	