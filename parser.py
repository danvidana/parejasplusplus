import sys
import ply.yacc as yacc
from scanner import tokens

# function for program
def p_program(p):
    '''program : PROGRAM ID SEMICOLON main
    | PROGRAM ID SEMICOLON vars main
    | PROGRAM ID SEMICOLON funcs main
    | PROGRAM ID SEMICOLON vars funcs main
    '''

# funciton for main
def p_main(p):
    'main : MAIN OPEN_PAREN CLOSE_PAREN block'

# function for funcs
def p_funcs(p):
    'funcs : func_type MODULE ID OPEN_PAREN var_type ID CLOSE_PAREN vars block'

# function for block
def p_block(p):
    'block : OPEN_BRACES statements CLOSE_BRACES'

# function for func_type
def p_func_type(p):
    '''func_type : var_type
    | VOID
    '''

# function for var_types
def p_var_type(p):
    '''var_type : INT
    | FLOAT
    | CHAR
    '''

# function for vars
def p_vars(p):
    'vars : VARS var_comp'
    
# function for var_comp, comp refers to complement
def p_var_comp(p):
    '''var_comp : var_type ids var_comp SEMICOLON var_comp
    | COMMA ids var_comp
    | empty
    '''

# function for ids
def p_ids(p):
    '''ids : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS
    | ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS
    | ID
    '''

# function for statements
def p_statements(p):
    '''statements : assignment statements
    | read statements
    | write statements
    | condition statements
    | return statements
    | func_call statements
    | empty
    '''

# function for assignments
def p_assignment(p):
    'assignment : ids ASSIGN expressions SEMICOLON'

# function for reads
def p_read(p):
    'read : READ OPEN_PAREN ids read_comp CLOSE_PAREN SEMICOLON'

# function for read_complementary
def p_read_comp(p):
    '''read_comp : COMMA ids read_comp
    | empty
    '''

# function for write
def p_write(p):
    '''write : WRITE OPEN_PAREN CT_STRING write_comp CLOSE_PAREN
    | WRITE OPEN_PAREN expressions write_comp CLOSE_PAREN
    '''

# function for write_complementary
def p_write_comp(p):
    '''write_comp : COMMA CT_STRING write_comp
    | COMMA expressions write_comp
    | empty
    '''

# function for condition
def p_condition(p):
    '''condition : IF OPEN_PAREN expressions CLOSE_PAREN THEN block ELSE block
    | IF OPEN_PAREN expressions CLOSE_PAREN THEN block
    | WHILE OPEN_PAREN expressions CLOSE_PAREN DO block
    | FOR ids ASSIGN expressions TO expressions DO block
    '''

# function for return
def p_return(p):
    'return : RETURN OPEN_PAREN exp CLOSE_PAREN SEMICOLON'

# funciton for func_call
def p_func_call(p):
    'func_call : ID OPEN_PAREN func_call_comp CLOSE_PAREN SEMICOLON'

# function for func_call_complementary
def p_func_call_comp(p):
    '''func_call_comp : ID func_call_comp
    | COMMA ID func_call_comp
    | empty
    '''

# function for expressions
def p_expressions(p):
    'expressions : exp expressions_op exp'

# function for expression operators
def p_expressions_op(p): 
    '''expressions_op : LESS_THAN
    | MORE_THAN
    | EQUALS
    | NOT_EQUALS
    | AND
    | OR
    '''

# function for exp
def p_exp(p):
    'exp : term exp_comp'

# function for exp_complementary
def p_exp_comp(p):
    '''exp_comp : PLUS exp
    | MINUS exp
    | empty
    '''

# function for term
def p_term(p):
    'term : factor term_comp'

# function for term_complimentary
def p_term_comp(p):
    '''term_comp : MULTIPLIES term
    | DIVIDE term
    | empty
    '''

# function for factor 
def p_factor(p):
    '''factor : OPEN_PAREN expressions CLOSE_PAREN
    | factor_comp ID
    | factor_comp func_call
    '''

# function for factor_complimentary
def p_factor_comp(p):
    '''factor_comp : PLUS
    | MINUS
    '''

# function for empty
def p_empty(p):
    'empty :'
    pass

# function for error 
def p_error(p):
    print(p)

yacc.yacc()

file = sys.argv[1]
f = open(file, 'r')
data = f.read()
f.close()
yacc.parse(data)
if yacc.parse(data) == "invalid":
	print("Sintax error")
