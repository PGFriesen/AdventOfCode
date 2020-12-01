#!/usr/bin/env python3

import os
import sys

def CreateProgram(args):
    name = "PythonTemplate.py"
    input_file = "input.txt"

    if len(args) >= 2:
        name = args[1]
    if len(args) >= 3:
        input_file = args[2]

    numFunctions = int(args[0])

    f = open(name, 'w')
    f.write("#!/usr/bin/env python3\n\nimport os\nimport sys\n\n")
    f.write("def readFile(input_file):\n    f = open(input_file, 'r')\n    return f.readlines()\n\n\n")
    for i in range(numFunctions):
        f.write("def function{}():\n    print(\"function placeholder\")\n\n\n".format(i+1))

    f.write("def main(arguments):\n    content = readFile('{}')\n\n\n".format(input_file))
    f.write("if __name__ == '__main__':\n    sys.exit(main(sys.argv[1:]))\n")
    f.close()

'''
The main program that takes in number of functions and
'''
def main(arguments):
    if len(arguments) >= 1:
        if (arguments[0] == "--help" or arguments[0] == "-h"):
            print("\nUsage:\n  '$ python3 pythonTemplateCreator.py <numbOfFunctions> <nameOfProgram> <nameOfInputFile>'\n\nParameters:\n  numOfFunctions: Required, the number of functions to create\n  nameOfProgram: Optional, name of program being created\n  nameOfInputFile: Optional, name of input file that the program will use\n")

        elif isinstance(int(arguments[0]),int):
            print("\n\nRunning...\n")
            CreateProgram(arguments)

        else:
            print("Unexpected Error, terminating\n")
        
    else:
        print("\nNo Arguments received")
        print("Usage:\n  '$ python3 pythonTemplateCreator.py <numbOfFunctions> <nameOfProgram> <nameOfInputFile>'\n\nParameters:\n  numOfFunctions: Required, the number of functions to create\n  nameOfProgram: Optional, name of program being created\n  nameOfInputFile: Optional, name of input file that program will use\n")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
