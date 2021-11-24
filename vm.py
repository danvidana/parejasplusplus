import sys
import parser

# Send file for build
file = sys.argv[1]
parser.build(file)

# Get quads, ct table and dirFunc from data.txt
file = open("data.txt", 'r')
data = eval(file.read())
file.close()

quadruples = data['quadruples']
ct_table = data['ct_table']
dirFunc = data['dirFunc']

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

memStack = Stack()

globalProgMem = Mem()
newMem = Mem()

GLOBAL_OVERFLOW = 35000
LOCAL_OVERFLOW = 70000



def inp_type(input_data):
    try:
        return type(eval(input_data))
    except (ValueError, SyntaxError):
        return str

def in_range(address, value_type):
    if value_type == type(1):
        if address in range(0,5000) or address in range(35000, 40000):
            return True
        else:
            return False
    elif value_type == type(1.0):
        if address in range(5000,10000) or address in range(40000, 45000):
            return True
        else:
            return False
    elif value_type == type('a'):
        if address in range(5000,10000) or address in range(40000, 45000):
            return True
        else:
            return False

# Get value from memory
def get_mem_value(address):
    value = ''
    if (address >= GLOBAL_OVERFLOW) and (address < LOCAL_OVERFLOW):
        try:
            value = memStack.peek().get_value(address)
        except:
            print("Error: Value not in memory")
    else:
        try:
            value = globalProgMemStack.get_value(address)
        except:
            print("Error: Value not in memory")

# Cast value to type depending on address
def get_value(address):
    if address in range(0,5000) or address in range(35000, 40000):
        return int(get_mem_value(address))
    elif address in range(5000,10000) or address in range(40000, 45000):
        return float(get_mem_value(address))
    elif address in range(5000,10000) or address in range(40000, 45000):
        return get_mem_value(address)
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

def run(ins_pointer = 0):
    currentQuad = quadruples[ins_pointer]
    ins = ''
    memStack.push(newMem)

    def goto():
        ins_pointer = currentQuad[3]
        return ins_pointer

    def gotoF():
        if currentQuad[1] == False:
            ins_pointer = currentQuad[3]
        else:
            ins_pointer += 1

        return ins_pointer





    def write():
        print(get_value(currentQuad[3]))
        ins_pointer += 1
        return ins_pointer

    def read():
        if value := input()
            valueType = inp_type(value)
