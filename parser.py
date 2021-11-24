import sys
import ply.yacc as yacc
from scanner import tokens
from semantic_cube import semantic_cube

# Stack Implementation
class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
     def elements(self):
        return self.items

# Global variables (directories, tables)

dirFunc = {}

currentId = ''
currentType = ''
currentFunc = ''

### Stacks for quadruples
# For expresions
operatorStack = Stack()
typeStack = Stack()
elementStack = Stack()
jumpStack = Stack()

funcName = 'global'


quadruples = []


# function for program
def p_program(p):
   '''program : PROGRAM ID add_program SEMICOLON vars funcs main end_program'''
    
def p_add_program(p):
    'add_program : '
    # Create dirFunc
    global dirFunc
    dirFunc[funcName] = {
        'type': 'void',
        'var_table': {},
        'next_int': 1,
        'next_float': 5000,
        'next_char': 10000,
        'next_temp_int': 15000,
        'next_temp_float': 20000,
        'next_temp_char': 25000,
        'next_temp_bool': 30000
    }
    #print(dirFunc)

def p_end_program(p):
    '''end_program : '''
    print(dirFunc)
    count = 0
    
    for x in quadruples:
        print(count,x)
        count += 1
    
# funciton for main
def p_main(p):
    'main : MAIN OPEN_PAREN CLOSE_PAREN block'

# function for funcs
def p_funcs(p):
    '''funcs : func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars block
    | empty
    '''

def p_add_module(p):
    '''add_module :'''
    global funcName
    idName = p[-1]
    # si funcion no es void y no existe como variable guardarla en vars globales para tener direccion a su resultado
    if currentType != 'void' and dirFunc[funcName]:
        funcAddress = set_address('global', currentType)
        dirFunc['global']['var_table'][idName] = {'type': currentType, 'address': funcAddress}

    

    funcName = idName
    if funcName not in dirFunc.keys():
        dirFunc[funcName] = {'type': currentType, 'var_table': {}}
    else:
        print('Error: Module ' + funcName + ' already defined')

# function for funcs_complementary
def p_funcs_comp(p):
    'funcs_comp : ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars block'

# function for funcs_params
def p_funcs_params(p):
    '''funcs_params : var_type variable_params funcs_params_comp
    | empty
    '''

# function for funcs_params_complementary
def p_funcs_params_comp(p):
    '''funcs_params_comp : COMMA var_type variable_params funcs_params_comp
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
    global currentType
    if p[1] == 'void':
        currentType = p[1]

# function for var_types
def p_var_type(p):
    '''var_type : INT
    | FLOAT
    | CHAR
    '''
    global currentType
    currentType = p[1]
    #print("currentType in p_var-type: " + currentType)

# function for vars
def p_vars(p):
    '''vars : VARS var_comp
    | empty
    '''

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
    idName = p[1]
    if idName not in dirFunc[funcName]["var_table"]:
        dirFunc[funcName]["var_table"][idName] = {
                'type': currentType,
                'address': set_address(funcName, currentType)
            }
    else:
        print('Error: Variable ' + idName + ' already defined')

# function for ids
def p_ids(p):
    '''ids : ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETS
    | ID OPEN_BRACKETS exp CLOSE_BRACKETS
    | ID
    '''
    global currentId
    currentId = p[1]

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
    global currentId
    result = elementStack.pop()
    resultType = typeStack.pop()
    
    if currentId in dirFunc[funcName]['var_table']:
        currentType = dirFunc[funcName]['var_table'][currentId]['type']
        assignType = semantic_cube[currentType]['='][resultType]
        if assignType != None:
            quadruples.append(['=', result, None, currentId])
            print(['=', result, None, currentId])
        else:
            print("Error: Assignment type mismatch")
    else:
        print("Error: Id not defined in current scope")

# function for reads
def p_read(p):
    'read : READ OPEN_PAREN ids g_quad_read read_comp CLOSE_PAREN' 
    

# function for read_complementary
def p_read_comp(p):
    '''read_comp : COMMA ids g_quad_read read_comp
    | empty 
    '''

# function for creating read quad
def p_g_quad_read(p):
    'g_quad_read : '
    # Get current type to assign address
    currentType = dirFunc[funcName]['var_table'][currentId]['type']
    tempAddress = set_address(funcName, 'temp_' + currentType)
    # generate quads to read in execution and then assign the temporal to the currentId
    quadruples.append(['read', None, None, tempAddress])
    quadruples.append(['=', tempAddress, None, currentId])

# function for write
def p_write(p):
    '''write : WRITE OPEN_PAREN CT_STRING g_quad_write_str write_comp CLOSE_PAREN
    | WRITE OPEN_PAREN expressions g_quad_write write_comp CLOSE_PAREN
    '''

# function for write_complementary
def p_write_comp(p):
    '''write_comp : COMMA CT_STRING g_quad_write_str write_comp
    | COMMA expressions g_quad_write write_comp
    | empty
    '''

# funtcion for generating write quad on ct strings
def p_g_quad_write_str(p):
    'g_quad_write_str : '
    # generate quadruple on past read str
    quadruples.append(['write', None, None, p[-1]])

# funtcion for generating write quad on variables
def p_g_quad_write(p):
    'g_quad_write : '
    # generate quadreuple on currentId
    quadruples.append(['write', None, None, currentId])

# Function to fill final goto of IF
def p_end_if(p):
    '''end_if : '''
    end = jumpStack.pop()
    fill(end, len(quadruples))

# function for condition
def p_condition(p):
    '''condition : IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block end_if
    | IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block ELSE g_else_quad block end_if
    | WHILE while_jump OPEN_PAREN expressions CLOSE_PAREN g_while_quad DO block end_while
    | FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block
    '''

# Function to generate quadruple for IF condition (gotoF)
def p_g_if_quad(p):
    '''g_if_quad :'''
    expressionType = typeStack.pop()
    if expressionType != 'bool':
        print('Error: Type Mismatch: IF condition must receive a BOOL type')
    else:
        result = elementStack.pop()
        quadruples.append(['gotoF',result,None,None])
        print(['gotoF',result,None,None])
        jumpStack.push(len(quadruples) - 1)

# Function to generate quadruple for IF-ELSE (goto)
def p_g_else_quad(p):
    '''g_else_quad :'''
    global jumpStack
    quadruples.append(['goto',None,None,None])
    quadToFill = jumpStack.pop()
    fill(quadToFill, len(quadruples))
    jumpStack.push(len(quadruples) - 1)

# Function to fill goto, gotoF 
def fill(end, cont):
    quadruples[end][3] = cont

# Function to save WHILE quadruple position
def p_while_jump(p):
    '''while_jump :'''
    jumpStack.push(len(quadruples))

# Function to generate quadruple for WHILE condition (gotoF)
def p_g_while_quad(p):
    '''g_while_quad :'''
    expressionType = typeStack.pop()
    if expressionType != 'bool':
        print('Error: Type Mismatch: WHILE condition must receive a BOOL type')
    else:
        result = elementStack.pop()
        quadruples.append(['gotoF',result,None,None])
        jumpStack.push(len(quadruples) - 1)

def p_end_while(p):
    '''end_while :'''
    end = jumpStack.pop()
    result = jumpStack.pop()
    quadruples.append(['goto',None,None,result])
    fill(end, len(quadruples))

# Function that validates if for definition is valid
def p_validate_for(p):
    '''validate_for :'''
    global currentId
    elementStack.push(currentId)
    idType = diFunc[funcName]["var_table"][currentId]["type"]
    if idType == 'int' or id == 'float':
        typeStack.push(diFunc[funcName]["var_table"][currentId]["type"])
    else:
        print("Error: Type Mismatch: FOR ID must be type INT or type FLOAT")

def p_for_counter_control(p):
    '''for_counter_control :'''
    expressionType = typeStack.pop()
    if expressionType == 'int' or expressionType == 'float':
        exp = elementStack.pop()
        vControl = elementStack.peek()
        controlType = typeStack.peek()
        tipoRes = semantic_cube[controlType]['='][expressionType]
        if tipoRes != None:
            quadruples.append(['=', exp, None, vControl])
        else:
            print("Error: Type Mismatch: FOR statement variables must match")
    else:
        print("Error: Type Mismatch: FOR expression must calculate INT or FLOAT")

def p_for_counter_end(p):
    '''for_counter_end :'''
    expressionType = typeStack.pop()
    if expressionType == 'int' or expressionType == 'float':
        exp = elementStack.pop()
        quadruples.append(['=',exp,None,exp])
        quadruples.append(['<',])

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
    '''expression_comp_3 : exp expressions_op exp g_quad_logic
    | exp
    '''

def p_g_quad_logic(p):
    'g_quad_logic : '
    generate_quadruple(['<','<=','>','>=','==','!='])

# function for expression operators
def p_expressions_op(p): 
    '''expressions_op : LESS_THAN add_op
    | LESS_THAN_EQUAL add_op
    | MORE_THAN add_op
    | MORE_THAN_EQUAL add_op
    | EQUALS add_op
    | NOT_EQUALS add_op
    '''
    

# function for exp
def p_exp(p):
    '''exp : term g_quad_exp_as
    | term g_quad_exp_as exp_comp
    '''

# Function for generating add and subtract quad
def p_g_quad_exp_as(p):
    'g_quad_exp_as : '
    generate_quadruple(['+','-'])

# function for exp_complementary (Sums and subtractions)
def p_exp_comp(p):
    '''exp_comp : PLUS add_op exp
    | MINUS add_op exp
    '''

# function for term
def p_term(p):
    '''term : factor g_quad_exp_md
    | factor g_quad_exp_md term_comp
    '''

# Function for generating multiply and divide quad
def p_g_quad_exp_md(p):
    'g_quad_exp_md : '
    generate_quadruple(['*','/'])

# function for term_complimentary (Multiplications and divisions)
def p_term_comp(p):
    '''term_comp : MULTIPLIES add_op term
    | DIVIDE add_op term
    '''

def p_add_op(p):
    'add_op : '
    operatorStack.push(p[-1])

# function to create quadruples for expressions
def generate_quadruple(operators):
    if operatorStack.size() > 0:
        temp = operatorStack.pop()
        operatorStack.push(temp)

        if temp in operators:
            # When operator in stack matches operators in precedence order pop from each stack the results
            rightOperand = elementStack.pop()
            rightType = typeStack.pop()
            leftOperand = elementStack.pop()
            letfType = typeStack.pop()
            operator = operatorStack.pop()

            resultType = semantic_cube[letfType][operator][rightType]
            if resultType != None:
                result = set_address(funcName, 'temp_' + resultType)
                quadruples.append([operator, leftOperand, rightOperand, result])
                print([operator, leftOperand, rightOperand, result])
                elementStack.push(result)
                typeStack.push(resultType)
            else:
                print("Error: Type mismatch")
                
# Function to set address for variables, even when temp
def set_address(funcName, typeValue):

    # address for global and main vars
    if funcName == 'global' or funcName == 'main':
        # match to types to decide which next address is needed
        match typeValue:
            case 'int':
                address = dirFunc[funcName]['next_int']
                # if address is higher than limit throw error
                if address > 4999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_int'] += 1

            case 'float':
                address = dirFunc[funcName]['next_float']
                # if address is higher than limit throw error
                if address > 9999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_float'] += 1
                
            case 'char':
                address = dirFunc[funcName]['next_char']
                # if address is higher than limit throw error
                if address > 14999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_char'] += 1
                
            case 'temp_int':
                address = dirFunc[funcName]['next_temp_int']
                # if address is higher than limit throw error
                if address > 19999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_temp_int'] += 1

            case 'temp_float':
                address = dirFunc[funcName]['next_temp_float']
                # if address is higher than limit throw error
                if address > 24999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_temp_float'] += 1
            
            case 'temp_char':
                address = dirFunc[funcName]['next_temp_char']
                # if address is higher than limit throw error
                if address > 29999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_temp_char'] += 1

            case 'temp_bool':
                address = dirFunc[funcName]['next_temp_bool']
                # if address is higher than limit throw error
                if address > 34999:
                    print("Error: Stack overflow")
                dirFunc[funcName]['next_temp_bool'] += 1

            case default:
                print('Error: Type value not available, global addresses.')

    return address

                
        

# function for factor 
def p_factor(p):
    '''factor : OPEN_PAREN add_fake expressions CLOSE_PAREN rem_fake
    | variable 
    | func_call
    | CT_INT add_ct_int
    | CT_FLOAT add_ct_float
    | CT_CHAR add_ct_char
    '''

def p_add_fake(p):
    'add_fake : '
    operatorStack.push(p[-1])

def p_rem_fake(p):
    'rem_fake : '
    operatorStack.pop()

# 3 Functions to push constants to stacks
def p_add_ct_int(p):
    'add_ct_int : '
    element = p[-1]
    
    elementStack.push(p[-1])
    typeStack.push('int')
    

def p_add_ct_float(p):
    'add_ct_float : '
    element = p[-1]
    
    elementStack.push(p[-1])
    typeStack.push('float')

def p_add_ct_char(p):
    'add_ct_char : '
    element = p[-1]
    
    elementStack.push(p[-1])
    typeStack.push('char')

# function for variable
def p_variable_params(p):
    '''variable_params : ID
    | ID dim
    '''

# function for variable
def p_variable(p):
    '''variable : ID add_id
    | ID dim
    '''

# function to add id to quads
def p_add_id(p):
    'add_id : '
    global currentId
    currentId = p[-1]

    # Check if variable exists, if exists it adds to stack
    if currentId in dirFunc[funcName]['var_table']:
        varName = currentId
        varType = dirFunc[funcName]['var_table'][currentId]['type']
        elementStack.push(varName)
        typeStack.push(varType)
    elif currentId in dirFunc['global']['var_table']:
        varName = currentId
        varType = dirFunc['global']['var_table'][currentId]['type']
        elementStack.push(varName)
        typeStack.push(varType)
    else:
        print('Error: Variable ' + currentId + ' not defined')

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
# if result == "valid":
# 	print("Valid input")
# else:
#     print("Inalid input")
