tokens = (
    "ID",
    "NUMBER",
    "SEMICOLON",
    "COMMA",
    "PROGRAM",
    "VARS",
    "MODULE",
    "INT",
    "FLOAT",
    "BOOLEAN",
    "VOID",
    "OPEN_PAREN",
    "CLOSE_PAREN",
    "OPEN_BRACKETS",
    "CLOSE_BRACKETS",
    "OPEN_BRACES",
    "CLOSE_BRACES",
    "EQUALS",
    "PLUS",
    "MINUS",
    "MULTIPLIES",
    "DIVIDE",
    "LESS_THAN",
    "MORE_THAN",
    "IF",
    "THEN",
    "ELSE",
    "WHILE",
    "DO",
    "FOR",
    "TO",
    "READ",
    "WRITE",
    "MAIN",
    "RETURN"
)

"""t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'"""

t_NUMBER = r'[0-9]+'

t_SEMICOLON = r";"

t_COMMA = r","

t_PROGRAM = r"program"

t_VARS = r"vars"

t_MODULE = r"module"

t_INT = r"int"

t_FLOAT = r"float"

t_BOOLEAN = r"bool"

t_VOID = r"void"

t_OPEN_PAREN = r"\("

t_CLOSE_PAREN = r"\("

t_OPEN_BRACKETS = r"\["

t_CLOSE_BRACKETS = r"\]"

t_OPEN_BRACES = r"\{"

t_CLOSE_BRACES = r"\}"

t_EQUALS = r"="

t_PLUS = r"\+"

t_MINUS = r"-"

t_MULTIPLIES = r"\*"

t_DIVIDE = r"/"

t_LESS_THAN = r"<"

t_MORE_THAN = r">"

t_IF = r"if"

t_THEN = r"then"

t_ELSE = r"else"

t_WHILE = r"while"

t_DO = r"do"

t_FOR = r"for"

t_TO = r"to"

t_READ = r"read"

t_WRITE = r"write"

t_MAIN = r"main"

t_RETURN = r"return"

t_ignore = ' \t'

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

# Build the lexer
import lex
lex.lex()

# Parsing rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLIES', 'DIVIDE')
)

# dictionary of names
names = {}

def p_program(t):
    'program : PROGRAM ID SEMICOLON VARS block'
    print(t[1])

######################################################## TODO: GRAMMAR ##############################################################

lex.input("while else if")
for tok in iter(lex.token, None):
    print(repr(tok.type), repr(tok.value))
