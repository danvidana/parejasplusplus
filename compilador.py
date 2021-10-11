import lex

tokens = (
    "IF",
    "ELSE",
    "FOR",
    "INT",
    "STRING",
    "WHILE",
    "SYMBOL",
    "COUNT",
    "IDENTIFIER"
)

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_IF = r"if"

t_ELSE = r"else"

t_FOR = r"for"

t_INT = r"int"

t_STRING = r"string"

t_WHILE = r"while"



t_ignore = ' \t'

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()

lex.input("while else if")
for tok in iter(lex.token, None):
    print(repr(tok.type), repr(tok.value))
