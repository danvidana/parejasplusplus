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
currentIdVar = ''
paramsCounter = 0
varsCounter = 0
funcCallCounter = 0

### Stacks for quadruples
# For expresions
operatorStack = Stack()
typeStack = Stack()
elementStack = Stack()
jumpStack = Stack()

funcName = 'global'


quadruples = []

# constant table
ct_table = {
	'next_ct_int': 70000,
	'next_ct_float': 75000,
	'next_ct_char': 80000,
	'next_ct_string': 85000
}

# function for program
def p_program(p):
   '''program : PROGRAM g_main_quad ID add_program SEMICOLON vars funcs main end_program'''
    
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

    print(ct_table)
    
# funciton for main
def p_main(p):
    'main : MAIN OPEN_PAREN CLOSE_PAREN fill_main_quad block'

def p_g_main_quad(p):
    'g_main_quad :'
    global funcName
    funcName = 'global'
    quadruples.append(['goto', None, None, None])

def p_fill_main_quad(p):
    'fill_main_quad :'
    fill(0, len(quadruples))

# function for funcs
def p_funcs(p):
    '''funcs : func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcs
    | empty
    '''

def p_end_funcs(p):
    'end_funcs :'
    global funcName
    temp_int_amount = dirFunc[funcName]['next_temp_int'] - 50000
    temp_float_amount = dirFunc[funcName]['next_temp_float'] - 55000
    temp_char_amount = dirFunc[funcName]['next_temp_char'] - 60000
    temp_bool_amount = dirFunc[funcName]['next_temp_bool'] - 65000
    dirFunc[funcName]["temporal_variables"] = temp_int_amount + temp_float_amount + temp_char_amount + temp_bool_amount
    quadruples.append(['endfunc', None, None, None])
    funcName = 'global'

def p_count_local_vars(p):
    'count_local_vars :'
    global dirFunc, funcName, varsCounter
    for x in dirFunc[funcName]["var_table"]:
        varsCounter += 1
    varsCounter -= dirFunc[funcName]["parameters"]
    dirFunc[funcName]["variables"] = varsCounter
    dirFunc[funcName]["quadruple_count"] = len(quadruples)
    varsCounter = 0

def p_add_module(p):
    '''add_module :'''
    global funcName
    idName = p[-1]

    funcName = idName
    if funcName not in dirFunc.keys():
        dirFunc[funcName] = {
            'type': currentType,
            'var_table': {},
            'parameter_table': [],
            'parameters': 0,
            'next_int': 35000,
            'next_float': 40000,
            'next_char': 45000,
            'next_temp_int': 50000,
            'next_temp_float': 55000,
            'next_temp_char': 60000,
            'next_temp_bool': 65000
            }
    else:
        print('Error: Module ' + funcName + ' already defined')

    # si funcion no es void y no existe como variable guardarla en vars globales para tener direccion a su resultado
    if currentType != 'void' and dirFunc[funcName]:
        funcAddress = set_address('global', currentType)
        dirFunc['global']['var_table'][idName] = {'type': currentType, 'address': funcAddress}

# function for funcs_complementary
def p_funcs_comp(p):
    'funcs_comp : ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcs'

def p_add_parameter_amount(p):
    'add_parameter_amount :'
    global dirFunc, funcName, paramsCounter
    dirFunc[funcName]["parameters"] = paramsCounter
    paramsCounter = 0

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

# function for variable
def p_variable_params(p):
    '''variable_params : ID
    | ID dim
    '''
    global currentId, currentType, paramsCounter
    paramsCounter += 1
    currentId = p[1]
    funcAddress = set_address(funcName, currentType)
    dirFunc[funcName]['var_table'][currentId] = {'type': currentType, 'address': funcAddress}
    parameterType = dirFunc[funcName]["var_table"][currentId]["type"]
    dirFunc[funcName]["parameter_table"].append({'name': currentId, 'type': parameterType})
    
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
            resultAddress = get_address(funcName, currentId)
            assignAddress = get_address(funcName, result)
            quadruples.append(['=', assignAddress, None, resultAddress])
        else:
            print("Error: Assignment type mismatch")
    else:
        print("Error: " + currentId + " not defined in current scope")

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

    resultAddress = get_address(funcName, currentId)
    # generate quads to read in execution and then assign the temporal to the currentId
    quadruples.append(['read', None, None, tempAddress])
    quadruples.append(['=', tempAddress, None, resultAddress])

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
    # generate quadruple on past read str, also add ct_string value and address
    resultAddress = set_address(funcName, 'ct_string', p[-1])
    quadruples.append(['write', None, None, resultAddress])

# funtcion for generating write quad on variables
def p_g_quad_write(p):
    'g_quad_write : '
    # generate quadreuple on currentId
    resultAddress = get_address(funcName, currentId)
    quadruples.append(['write', None, None, resultAddress])

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
    | FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block end_for
    '''

# Function to generate quadruple for IF condition (gotoF)
def p_g_if_quad(p):
    '''g_if_quad :'''
    expressionType = typeStack.pop()
    if expressionType != 'bool':
        print('Error: Type Mismatch: IF condition must receive a BOOL type')
    else:
        result = elementStack.pop()
        resultAddress = get_address(funcName, result)
        quadruples.append(['gotoF',resultAddress,None,None])
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
    if currentId in dirFunc[funcName]["var_table"]:
        idType = dirFunc[funcName]["var_table"][currentId]["type"]
        if idType == 'int' or id == 'float':
            typeStack.push(dirFunc[funcName]["var_table"][currentId]["type"])
        else:
            print("Error: Type Mismatch: FOR ID must be type INT or type FLOAT")
    else:
        print("Error: Id not defined in current scope")


def p_for_counter_control(p):
    '''for_counter_control :'''
    expressionType = typeStack.pop()

    if expressionType == 'int' or expressionType == 'ct_int' or expressionType == 'float' or expressionType == 'ct_float':
        exp = elementStack.pop()
        vControl = elementStack.peek()
        controlType = typeStack.peek()
        tipoRes = semantic_cube[controlType]['='][expressionType]
        if tipoRes != None:
            if expressionType == 'ct_int' or expressionType == 'ct_float':
                expAddress = set_address(funcName, expressionType, exp)
            else:
                expAddress = get_address(funcName, exp)
            vControlAddress = get_address(funcName, vControl)
            quadruples.append(['=', expAddress, None, vControlAddress])
        else:
            print("Error: Type Mismatch: FOR statement variables must match")
    else:
        print("Error: Type Mismatch: FOR expression must calculate INT or FLOAT")

# Function for generating and managing quadruples that control cycles
def p_for_counter_end(p):
    '''for_counter_end :'''
    global funcName
    expressionType = typeStack.pop()
    if expressionType == 'int' or expressionType == 'ct_int' or expressionType == 'float' or expressionType == 'ct_float':
        exp = elementStack.pop()
        tInt = set_address(funcName, 'temp_int')
        if expressionType == 'ct_int' or expressionType == 'ct_float':
            expAddress = set_address(funcName, expressionType, exp)
        else:
            expAddress = get_address(funcName, exp)
        quadruples.append(['=', expAddress, None, tInt])
        vControl = elementStack.peek()
        tBool = set_address(funcName, 'temp_bool')
        vControlAddress = get_address(funcName, vControl)
        quadruples.append(['<', vControlAddress, tInt, tBool])
        jumpStack.push(len(quadruples) - 1)
        quadruples.append(['gotoF', tBool, None, None])
        jumpStack.push(len(quadruples) - 1)
    else:
        print("Error: Type Mismatch: FOR upper limit value must be INT or FLOAT")

# Function to generate FOR quadruples that increment the control
def p_end_for(p):
    '''end_for :'''
    vControl = elementStack.peek()
    tInt = set_address(funcName, 'temp_int')
    vControlAddress = get_address(funcName, vControl)
    constantControlAddress = set_address(funcName, 'ct_int', 1)
    quadruples.append(['+', vControlAddress, constantControlAddress, tInt])
    quadruples.append(['=', tInt, None, vControlAddress])
    fin = jumpStack.pop()
    ret = jumpStack.pop()
    quadruples.append(['goto', None, None, ret])
    fill(fin, len(quadruples))
    elimina = elementStack.pop()
    tipoElimina = typeStack.pop()

# function for return
def p_return(p):
    'return : RETURN OPEN_PAREN expressions CLOSE_PAREN return_end'

def p_return_end(p):
    'return_end :'
    quadruples.append(['return', funcName, None, funcName])

# funciton for func_call
def p_func_call(p):
    '''func_call : ID verify_function_exists OPEN_PAREN era_activation func_call_comp CLOSE_PAREN g_gosub_quad change_to_global
    '''

def p_g_gosub_quad(p):
    'g_gosub_quad :'
    quadruples.append(['gosub',None , None, funcName])

def p_change_to_global(p):
    'change_to_global :'
    global funcName
    funcName = 'global'

def p_verify_function_exists(p):
    'verify_function_exists :'
    global currentId, funcName
    funcName = p[-1]
    nameId = p[-1]
    currentId = nameId
    print(p[-1])
    if nameId not in dirFunc:
        print("Error: Wrong Function Call: " + nameId + " function does not exist")

def p_era_activation(p):
    'era_activation :'
    global currentId
    quadruples.append(['ERA', None, None, currentId])
    counter = 0

# function for func_call_complementary
def p_func_call_comp(p):
    '''func_call_comp : expressions g_parameter_quad func_call_comp
    | COMMA expressions g_parameter_quad func_call_comp
    | empty
    '''

def p_g_parameter_quad(p):
    'g_parameter_quad :'
    global funcCallCounter
    argument = elementStack.pop()
    print(argument)
    argumentType = typeStack.pop()
    if argumentType == dirFunc[funcName]["parameter_table"][funcCallCounter]["type"]:
        quadruples.append(['param', argument, None, dirFunc[funcName]["parameter_table"][funcCallCounter]["name"]])
    else:
        print("Error: Type Mismatch: Argument provided is not same type as parameter")
    if funcCallCounter < dirFunc[funcName]["parameters"] - 1:
        funcCallCounter += 1


def p_parameter_check_comma(p):
    'parameter_check_comma :'


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
    '''exp : term g_quad_exp_as_alone
    | term g_quad_exp_as exp_comp
    '''

# Function for generating add and subtract quad
def p_g_quad_exp_as(p):
    'g_quad_exp_as : '
    generate_quadruple(['+','-'])

def p_g_quad_exp_as_alone(p):
    'g_quad_exp_as_alone : '
    generate_quadruple(['+','-'],True)

# function for exp_complementary (Sums and subtractions)
def p_exp_comp(p):
    '''exp_comp : PLUS add_op exp
    | MINUS add_op exp
    '''

# function for term
def p_term(p):
    '''term : factor g_quad_exp_md_alone
    | factor g_quad_exp_md term_comp
    '''

# Function for generating multiply and divide quad
def p_g_quad_exp_md(p):
    'g_quad_exp_md : '
    generate_quadruple(['*','/'])

# Function for generating multiply and divide quad if operand is alone
def p_g_quad_exp_md_alone(p):
    'g_quad_exp_md_alone : '
    generate_quadruple(['*','/'],True)

# function for term_complimentary (Multiplications and divisions)
def p_term_comp(p):
    '''term_comp : MULTIPLIES add_op term
    | DIVIDE add_op term
    '''

def p_add_op(p):
    'add_op : '
    operatorStack.push(p[-1])

# function to create quadruples for expressions
def generate_quadruple(operators, alone = False):
    if operatorStack.size() > 0:
        temp = operatorStack.pop()
        operatorStack.push(temp)

        if temp in operators:
            # When operator in stack matches operators in precedence order pop from each stack the results
            rightOperand = elementStack.pop()
            rightType = typeStack.pop()
            leftOperand = elementStack.pop()
            leftType = typeStack.pop()
            operator = operatorStack.pop()

            resultType = semantic_cube[leftType][operator][rightType]
            if rightType in ['ct_int', 'ct_float', 'ct_char']:
                # Add ct to ct_table
                rightAddress = set_address(rightOperand, rightType, rightOperand)
            elif alone:
                # Add expression to temp local table
                rightAddress = set_address(funcName, rightType)
            else:
                rightAddress = get_address(funcName, rightOperand)

            if leftType in ['ct_int', 'ct_float', 'ct_char']:
                # Add ct to ct_table
                leftAddress = set_address(leftOperand, leftType, leftOperand)
            elif alone:
                # Add expression to temp local table
                leftAddress = set_address(funcName, leftType)
            else:
                leftAddress = get_address(funcName, leftOperand)
                

            if resultType != None:
                resultAddress = set_address(funcName, 'temp_' + resultType)
                quadruples.append([operator, leftAddress, rightAddress, resultAddress])
                elementStack.push(resultAddress)
                typeStack.push(resultType)
            else:
                print("Error: Type mismatch")
                
# Function to set address for variables, even when temp
def set_address(funcName, typeValue, value=None):
    # var to know if its globals or locals
    localOrGlobal = 0
    if funcName != 'global':
        localOrGlobal = 35000

    # match to types to decide which next address is needed
    match typeValue:
        case 'int':
            address = dirFunc[funcName]['next_int'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 4999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_int'] += 1

        case 'float':
            address = dirFunc[funcName]['next_float'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 9999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_float'] += 1
            
        case 'char':
            address = dirFunc[funcName]['next_char'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 14999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_char'] += 1
            
        case 'temp_int':
            address = dirFunc[funcName]['next_temp_int'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 19999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_temp_int'] += 1

        case 'temp_float':
            address = dirFunc[funcName]['next_temp_float'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 24999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_temp_float'] += 1
        
        case 'temp_char':
            address = dirFunc[funcName]['next_temp_char'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 29999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_temp_char'] += 1

        case 'temp_bool':
            address = dirFunc[funcName]['next_temp_bool'] + localOrGlobal
            # if address is higher than limit throw error
            if address > 34999 + localOrGlobal:
                print("Error: Stack overflow")
            dirFunc[funcName]['next_temp_bool'] += 1
            
        case 'ct_int':
            address = ct_table['next_ct_int']
            ct_table[address] = value
            # if address is higher than limit throw error
            if address > 74999:
                print("Error: Stack overflow")
            ct_table['next_ct_int'] += 1
            
        case 'ct_float':
            address = ct_table['next_ct_float']
            ct_table[address] = value
            # if address is higher than limit throw error
            if address > 79999:
                print("Error: Stack overflow")
            ct_table['next_ct_float'] += 1
            
        case 'ct_char':
            address = ct_table['next_ct_char']
            ct_table[address] = value
            # if address is higher than limit throw error
            if address > 84999:
                print("Error: Stack overflow")
            ct_table['next_ct_char'] += 1

        case 'ct_string':
            address = ct_table['next_ct_string']
            ct_table[address] = value
            # if address is higher than limit throw error
            if address > 89999:
                print("Error: Stack overflow")
            ct_table['next_ct_string'] += 1

        case default:
            print('Error: Type value not available, global addresses.')

    return address

# function to get the address in the dirFunc for the quad
def get_address(funcName, idOrAddress):

    # check if id is in var table else, check if it is temporal
    if idOrAddress in dirFunc[funcName]['var_table']:
        address = dirFunc[funcName]['var_table'][idOrAddress]['address']
    else:
        address = idOrAddress


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
    typeStack.push('ct_int') 

def p_add_ct_float(p):
    'add_ct_float : '
    element = p[-1]
    
    elementStack.push(p[-1])
    typeStack.push('ct_float')

def p_add_ct_char(p):
    'add_ct_char : '
    element = p[-1]
    
    elementStack.push(p[-1])
    typeStack.push('ct_char')

# function for variable
def p_variable(p):
    '''variable : ID add_id
    | ID dim
    '''

# function to add id to quads
def p_add_id(p):
    'add_id : '
    global currentIdVar
    currentIdVar = p[-1]

    # Check if variable exists, if exists it adds to stack
    if currentIdVar in dirFunc[funcName]['var_table']:
        varName = currentIdVar
        varType = dirFunc[funcName]['var_table'][currentIdVar]['type']
        elementStack.push(varName)
        typeStack.push(varType)
    elif currentIdVar in dirFunc['global']['var_table']:
        varName = currentIdVar
        varType = dirFunc['global']['var_table'][currentIdVar]['type']
        elementStack.push(varName)
        typeStack.push(varType)
    else:
        print('Error: Variable ' + currentIdVar + ' not defined')

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

def build(file):
    global yacc 
    
    f = open(file, 'r')
    data = f.read()
    f.close()
    yacc.parse(data)

    file = open("data.txt",'w')

    data = {
        'quadruples' : quadruples,
        'ct_table' : ct_table,
        'dirFunc' : dirFunc
    }
    
    file.write(str(data))
    file.close()
# if result == "valid":
# 	print("Valid input")
# else:
#     print("Inalid input")

# to continue testing only parser
build(sys.argv[1])
