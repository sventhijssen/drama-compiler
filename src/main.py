import getopt
import sys

from Compiler import Compiler


def main(argv):
    """
    Source: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    :param argv:
    :return:
    """
    inputFileName = ''
    outputFileName = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFileName = arg
        elif opt in ("-o", "--ofile"):
            outputFileName = arg
    inputFile = open(inputFileName, "r")
    sourceCode = inputFile.read()
    compiler = Compiler(sourceCode)
    compiler.parse()
    compiler.compile()
    code = compiler.build()
    print(code)


if __name__ == '__main__':
    main(sys.argv[1:])
