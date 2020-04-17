from LexicalAnalyzer import TokenListForParser
from prettytable import PrettyTable
import re
import texttable as tt
from tabulate import tabulate
# Global Variables
index = 0
inpIndex = 0  # input pointer
nodeNum = 0  # number of node for graphviz
flage = 1
# Implentation of Stack
st = []
'''
inp=TokenListForParser

inp+='$'
'''



  # append dollar to the scanned input
mapper={'begin':'a','newline':'b','end':'c','print':'d','string':'e','datatype':'f','id':'g','comma':'h','equals':'i','number':'j','for':'k','to':'l'}
terminals = {'S\'': 'S\'', 'S': 'S', 'A': 'CODE', 'B': 'PRINTSTMT', 'C': 'DECLARATIONS', 'D': 'DEFINATIONS',
             'E': 'FORSTMT', 'F': 'DECLARATION2', 'G': 'DECLARATION1', 'I': 'INTDEFLIST', 'Z': 'STRDEFLIST', 'Y': 'INTDEF', 'Q': 'STRDEF'}
nonterminals = {'a': 'begin', 'b': 'newline', 'c': 'end', 'd': 'print', 'e': 'string',
                'f': 'datatype', 'g': 'id', 'h': 'comma', 'i': 'equals', 'j': 'number', 'k': 'for', 'l': 'to', '$': '$'}
action = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
          'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, '$': 12}
goto = {'S\'': 13, 'S': 14, 'A': 15, 'B': 16, 'C': 17, 'G': 18,
        'F': 19, 'D': 20, 'I': 21, 'Z': 22, 'Y': 23, 'Q': 24, 'E': 25}
inp=[]
for i in TokenListForParser:
    inp.append(mapper[i])




inp+='$'
print(inp)
str1=' '.join(inp)
print(str1)