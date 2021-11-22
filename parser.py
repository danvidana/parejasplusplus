import sys
import ply.yacc as yacc
from scanner import tokens

# Global variables (directories, tables)

dirFunc = {}

currentId = ''
currentType = ''
currentFunc = ''

funcName = 'global'

# function for program
def p_program(p):
    'program : PROGRAM ID SEMICOLON vars funcs main'
    # Create dirFunc
    global dirFunc
    dirFunc["program"]["name"] = p[2]
    dirFunc["program"]["type"] = 'void'
    
    
# funciton for main
def p_main(p):
    'main : MAIN OPEN_PAREN CLOSE_PAREN block'

# function for funcs
def p_funcs(p):
    '''funcs : func_type MODULE ID OPEN_PAREN funcs_params CLOSE_PAREN vars block
    | empty
    '''

# function for funcs_complementary
def p_funcs_comp(p):
    'funcs_comp : ID OPEN_PAREN funcs_params CLOSE_PAREN vars block'

# function for funcs_params
def p_funcs_params(p):
    '''funcs_params : var_type variable funcs_params_comp
    | empty
    '''

# function for funcs_params_complementary
def p_funcs_params_comp(p):
    '''funcs_params_comp : COMMA var_type ID funcs_params_comp
    | empty
    '''


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
    '''vars : VARS create_var_table var_comp
    | empty
    '''

def p_create_var_table(p):
    '''create_var_table : '''
    dirFunc[funcName] = {'vars':None}
    if(dirFunc[funcName]['vars'] == None):
        print("Sin tabla")
    
    
# function for var_comp, comp refers to complement
def p_var_comp(p):
    '''var_comp : var_type ids_dec var_comp_2 var_comp_final
    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive
    '''
    
def p_var_comp_2(p):
    '''var_comp_2 : COMMA ids_dec var_comp_3
    | empty
    '''

def p_var_comp_3(p):
    'var_comp_3 : var_comp_2'

def p_var_comp_recursive(p):
    '''var_comp_recursive : var_type ids_dec var_comp_2 var_comp_final
    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive
    '''

def p_var_comp_final(p):
    '''var_comp_final : SEMICOLON
    | var_module_trans
    '''

# Function for transition to functions in case module is found
def p_var_module_trans(p):
    '''var_module_trans : SEMICOLON var_type MODULE funcs_comp
    '''

# function for ids declarations
def p_ids_dec(p):
    '''ids_dec : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS
    | ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS
    | ID
    '''

# function for ids
def p_ids(p):
    '''ids : ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETS
    | ID OPEN_BRACKETS exp CLOSE_BRACKETS
    | ID
    '''

# Insers ID variable into symbol table
# def insert_id(p):
#     'insert_id : '
#     global currentId, currentType, currentFunc
#     currentId = p[-1]
#     if context == 'global':
#         d


# function for statements
def p_statements(p):
    '''statements : assignment SEMICOLON statements
    | read SEMICOLON statements 
    | write SEMICOLON statements
    | condition statements
    | return SEMICOLON statements
    | func_call SEMICOLON statements
    | empty
    '''

# function for assignments
def p_assignment(p):
    'assignment : ids ASSIGN expressions'

# function for reads
def p_read(p):
    'read : READ OPEN_PAREN ids read_comp CLOSE_PAREN'

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
    | FOR ids_dec ASSIGN expressions TO expressions DO block
    '''

# function for return
def p_return(p):
    'return : RETURN OPEN_PAREN exp CLOSE_PAREN'

# funciton for func_call
def p_func_call(p):
    '''func_call : ID OPEN_PAREN func_call_comp CLOSE_PAREN
    '''

# function for func_call_complementary
def p_func_call_comp(p):
    '''func_call_comp : expressions func_call_comp
    | COMMA expressions func_call_comp
    | empty
    '''

# function for expressions
def p_expressions(p):
    'expressions : expressions_comp'

# function for expressions_comp
def p_expressions_comp(p):
    '''expressions_comp : expression_comp_2
    | expression_comp_2 OR expressions_comp
    '''

# function for expressions_comp_2
def p_expression_comp_2(p):
    '''expression_comp_2 : expression_comp_3
    | expression_comp_3 AND expression_comp_2
    '''

# function for expressions_comp_3
def p_expression_comp_3(p):
    '''expression_comp_3 : exp
    | exp expressions_op exp
    '''

# function for expression operators
def p_expressions_op(p): 
    '''expressions_op : LESS_THAN
    | LESS_THAN_EQUAL
    | MORE_THAN
    | MORE_THAN_EQUAL
    | EQUALS
    | NOT_EQUALS
    '''

# function for exp
def p_exp(p):
    '''exp : term
    | term exp_comp
    '''

# function for exp_complementary (Sums and subtractions)
def p_exp_comp(p):
    '''exp_comp : PLUS exp
    | MINUS exp
    '''

# function for term
def p_term(p):
    '''term : factor 
    | factor term_comp
    '''

# function for term_complimentary (Multiplications and divisions)
def p_term_comp(p):
    '''term_comp : MULTIPLIES term
    | DIVIDE term
    '''

# function for factor 
def p_factor(p):
    '''factor : OPEN_PAREN expressions CLOSE_PAREN
    | variable
    | func_call
    | CT_INT
    | CT_FLOAT
    | CT_CHAR
    '''

# function for variable
def p_variable(p):
    '''variable : ID
    | ID dim
    '''

# function for variable
def p_dim(p):
    'dim : OPEN_BRACKETS exp CLOSE_BRACKETS'


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
