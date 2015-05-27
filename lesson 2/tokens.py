import re

def t_RANGLE(token):
	r'>'
	return token

def t_LANGLESLASH(token):
	r'</'
	return token
	

def t_NUMBER(token):
	r"[0-9]+"
	token.value = int(token.value)
	return token

print t_NUMBER(1368)

def t_STRING(token):
	r'"[^"]*"'
	return token

def t_WORD(token):
	r'[^ <>]+'
	return token