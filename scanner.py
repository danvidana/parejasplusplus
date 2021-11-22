import ply.lex as lex
import math

#Palabras reservadas

reserved = {
    'program': "PROGRAM",
    'main': "MAIN",
    'vars': "VARS",
    'int': "INT",
    'float': "FLOAT",
    'char': "CHAR",
    'module': "MODULE",
    'return': "RETURN",
    'read': "READ",
    'write': "WRITE",
    'if': "IF",
    'then': "THEN",
    'else': "ELSE",
    'while': "WHILE",
    'do': "DO",
    'for': "FOR",
    'to': "TO",
    'void': "VOID"
}

#Tokens

tokens = (
    "SEMICOLON",
    "COMMA",
    "PROGRAM",
    "VARS",
    "MODULE",
    "ID",
    "INT",
    "FLOAT",
    "BOOLEAN",
    "CHAR",
    "VOID",
    "OPEN_PAREN",
    "CLOSE_PAREN",
    "OPEN_BRACKETS",
    "CLOSE_BRACKETS",
    "OPEN_BRACES",
    "CLOSE_BRACES",
    "ASSIGN",
    "EQUALS",
    "NOT_EQUALS",
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
    "RETURN",
    "CT_INT",
    "CT_FLOAT",
    "CT_CHAR",
    "CT_STRING",
    "AND",
    "OR"
)

t_SEMICOLON = r";"
t_COMMA = r","
t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"
t_OPEN_BRACKETS = r"\["
t_CLOSE_BRACKETS = r"\]"
t_OPEN_BRACES = r"\{"
t_CLOSE_BRACES = r"\}"
t_ASSIGN = r"="
t_EQUALS = r'\=='
t_PLUS = r"\+"
t_MINUS = r"-"
t_MULTIPLIES = r"\*"
t_DIVIDE = r"/"
t_LESS_THAN = r"<"
t_MORE_THAN = r">"
t_AND = r"&&"
t_OR = r"\|\|"
t_NOT_EQUALS = r"!="

#Definiciones de TOKENS

#Cualquier ID (Empieza con letra/_ seguido por lo que sea)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

#Detecta si el numero es FLOAT o INT y asigna el valor correcto de la constante
def t_CT_FLOAT(t):
	r'([0-9]*[.])?[0-9]+'
	if int(math.floor(float(t.value))) == float(t.value):
		try:
			t.value = int(t.value)
			t.type = 'CT_INT'
		except ValueError:
			t.value = float(t.value)
	else:
		t.value = float(t.value)
	return t

#STRINGs para mostrar en write()
def t_CT_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CT_CHAR(t):
    r'\'.\''
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,t.lineno))

#Test para probar scanner

# data = '''
# program foreveralone;
# vars
#     int i, j, p;
#     int Arreglo[10];
#     float valor;
#     int Matriz[3][8];

# int module fact (int j)
# vars int i;
# {
#     i = j + (p - j*2.1+j);
#     if (j==1 && j !=2) then
#         {return (j);}
#     else
#         {return (j*fact(j-i));}
# }

# void module inicia (int y)
# var int x;
# {
#     x=1;
#     while(x < 11) do
#     {
#         Arreglo[x]=y*x;
#         x=x+1;
#     }
# }

# main ()
# {
#     read(p); j=p*2;
#     inicia(p*j - 5);
#     for i=1 to 10 do
#     {
#         Arreglo[i]=Arreglo[i]*fact(Arreglo[i]-p);
#     }
#     for j=1 to 3 do
#         for k=1 to 8 do
#         {
#             Matriz[j,k]=Arreglo[j+k-fact(p)+p*k]*p+j;
#         }
#     while(i >= 0) do
#         {
#             write("resultado", Arreglo[i], fact(i+2)*valor);
#             i=i - 1;
#         }
# }

# '''

lex.lex()

#Test para scanner

# lex.input(data)
# for tok in iter(lex.token, None):
#     print(repr(tok.type), repr(tok.value))
