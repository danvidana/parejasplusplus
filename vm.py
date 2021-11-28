import sys
import parser

# Send file for build
file = sys.argv[1]
parser.build(file)

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

class Mem:
    def __init__(self):
        self.addresses = {}

    def set_value(self, value, address):
        self.addresses[address] = value

    def get_value(self, address):
        if address in self.addresses:
            return self.addresses[address]
        print("ERROR: Address not found", address, self.addresses)
        raise CompilerError(f"ERROR: Address not found {address}")

    def get_values(self):
        return self.addresses

fCallsStack = Stack()
memStack = Stack()

globalProgMem = Mem()
newMem = Mem()
inERA = False

GLOBAL_OVERFLOW = 35000
LOCAL_OVERFLOW = 70000

currentFunc = 'global'

ins_pointer = 0

counter = {
    'int': 0,
    'float': 0,
    'char': 0
}

# Local base addresses
base_address = {
    'int': 35000,
    'float': 40000,
    'char': 45000
}

def inp_type(input_data):
    try:
        return type(eval(input_data))
    except (ValueError, SyntaxError):
        return str

def in_range(address, value_type):
    if value_type == type(1):
        global currentType
        if address in range(0,5000) or address in range(15000,20000) or address in range(35000, 40000):
            currentType = type(1)
            return True
        else:
            return False
    elif value_type == type(1.0):
        if address in range(5000,10000) or address in range(20000,25000) or address in range(40000, 45000):
            currentType = type(1.0)
            return True
        else:
            return False
    elif value_type == type('a'):
        if address in range(5000,10000) or address in range(25000,30000) or address in range(40000, 45000):
            currentType = type('a')
            return True
        else:
            return False

# Get value from memory
def get_mem_value(address):
    value = 0
    # print(address)
    if (address >= GLOBAL_OVERFLOW) and (address < LOCAL_OVERFLOW):
        try:
            value = memStack.peek().get_value(address)
        except:
            print("Error: Value not in local memory")
    else:
        try:
            value = globalProgMem.get_value(address)
        except:
            print("Error: Value not in memory", address)

    return value

# Cast value to type depending on address
def get_value(address):
    if address in range(0,5000) or address in range(15000, 20000) or address in range(35000, 40000) or address in range(50000, 55000):
        return int(get_mem_value(address))
    elif address in range(5000,10000) or address in range(20000, 25000) or address in range(40000, 45000) or address in range(55000, 60000):
        return float(get_mem_value(address))
    elif address in range(10000,15000) or address in range(25000, 30000) or address in range(45000, 50000) or address in range(60000, 65000):
        return get_mem_value(address)
    elif address in range(70000,90000):
        return ct_table[address]
    else:
        return get_value(get_mem_value(address))

# Set the value in memory
def set_value(value, address):
    if address >= GLOBAL_OVERFLOW and address < LOCAL_OVERFLOW:
        memStack.peek().set_value(value, address)
    else:
        globalProgMem.set_value(value, address)

# Make result of expression
def get_result(leftOperand, operator, rightOperand):
    match operator:
        case '+':
            return leftOperand + rightOperand
        case '-':
            return leftOperand - rightOperand
        case '*':
            return leftOperand * rightOperand
        case '/':
            if isinstance(leftOperand, int) and isinstance(rightOperand, int):
                return leftOperand // rightOperand
            else:
                return leftOperand / rightOperand
        case '<':
            return leftOperand < rightOperand
        case '<=':
            return leftOperand <= rightOperand
        case '>':
            return leftOperand > rightOperand
        case '>=':
            return leftOperand >= rightOperand
        case '==':
            return leftOperand == rightOperand
        case '!=':
            return leftOperand != rightOperand
        case '&&':
            return leftOperand and rightOperand
        case '||':
            return leftOperand or rightOperand

def run_quad():
    global ins_pointer, newMem, currentFunc, counter, inERA
    currentQuad = quadruples[ins_pointer]
    ins = currentQuad[0]
    print(currentQuad)
    # memStack.push(newMem)

    # match against instruction of current quad to make operation
    match ins:
        case 'goto':
            ins_pointer = currentQuad[3]
            return ins_pointer

        case 'gotoF':
            if get_mem_value(currentQuad[1]) == False:
                ins_pointer = currentQuad[3]
            else:
                ins_pointer += 1

            return ins_pointer

        case 'ERA':
            newMem = Mem()
            inERA = True
            currentFunc = currentQuad[3]
            ins_pointer += 1
            return ins_pointer

        # quad = [param, address, None, paramName]
        case 'param':
            value = get_value(currentQuad[1])
            # print('value: ',value)
            paramType = dirFunc[currentFunc]['var_table'][currentQuad[3]]['type']
            address = base_address[paramType] + counter[paramType]
            counter[paramType] += 1
            newMem.set_value(value, address)
            # print(newMem.get_values())
            ins_pointer += 1
            return ins_pointer

            #param, 5020, None, 2003

        # quad = ['gosub',,,funcName]
        case 'gosub':
            counter = {
                "int": 0,
                "float": 0,
                "char": 0
            }
            ins_pointer += 1
            fCallsStack.push(ins_pointer)
            in_ERA = False
            # print('newMem values:',newMem.get_values())
            memStack.push(newMem)
            ins_pointer = currentQuad[3]
            return ins_pointer

        # quad = ['endfunc',,,]
        case 'endfunc':
            if not memStack.is_empty():
                memStack.pop()
            if not fCallsStack.is_empty():
                ins_pointer = fCallsStack.pop()
            else:
                ins_pointer += 1
            return ins_pointer

        # quad = ['write',,,address]
        case 'write':
            print(get_value(currentQuad[3]))
            ins_pointer += 1
            return ins_pointer

        # quad = ['read',,,address]
        case 'read':
            if value := input('Type input: '):
                valueType = inp_type(value)
                if in_range(currentQuad[3], valueType):
                    set_value(value, currentQuad[3])
                    ins_pointer += 1
                else:
                    print('ERROR: Not in range: ', value, currentQuad[3])

            return ins_pointer

        # quad = ['return',funcName,,address]
        case 'return':
            value = get_value(currentQuad[3])
            # print(value)
            currentFunc = currentQuad[1]
            memStack.pop()
            set_value(value, dirFunc['global']['var_table'][currentFunc]['address'])
            ins_pointer = fCallsStack.pop()
            return ins_pointer

        # quad = ['ver', address, address, address]
        case 'ver':
            value = get_value(currentQuad[1])
            if value in range(currentQuad[3]):
                ins_pointer += 1
            else:
                print('Error: Index out of bounds: ', value)
            return ins_pointer

        case '=':
            firstValue = get_value(currentQuad[1])
            if currentQuad[3] < 70000:
                set_value(firstValue, currentQuad[3])
            else:
                set_value(firstValue, ct_table[currentQuad[3]])
            
            ins_pointer += 1
            return ins_pointer

        case _:
            firstValue = get_value(currentQuad[1])
            secondValue = get_value(currentQuad[2])
            result = get_result(firstValue, ins, secondValue)
            
            
            set_value(result, currentQuad[3])
            ins_pointer += 1
            return ins_pointer



def start():
    # Get quads, ct table and dirFunc from data.txt
    with open(file + '.obj', 'r') as data:
        fileData = eval(data.read())
        global quadruples, ct_table, dirFunc
        quadruples = fileData['quadruples']
        ct_table = fileData['ct_table']
        dirFunc = fileData['dirFunc']

    # debugging       
    # counter = 0
    while ins_pointer < len(quadruples):
        # print(counter, quadruples[ins_pointer])
        run_quad()
        # counter += 1

start()