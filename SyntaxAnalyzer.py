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
             'E': 'FORSTMT', 'F': 'DECLARATION2', 'G': 'DECLARATION1', 'I': 'INTDEFLIST', 'Z': 'STRDEFLIST', 'Y': 'INTDEF', 'Q': 'STRDEF','X':'INTDEF2'}
nonterminals = {'a': 'begin', 'b': 'newline', 'c': 'end', 'd': 'print', 'e': 'string',
                'f': 'datatype', 'g': 'id', 'h': 'comma', 'i': 'equals', 'j': 'number', 'k': 'for', 'l': 'to', '$': '$'}
action = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
          'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, '$': 12}
goto = {'S\'': 13, 'S': 14, 'A': 15, 'B': 16, 'C': 17, 'G': 18,
        'F': 19, 'D': 20, 'I': 21, 'Z': 22, 'Y': 23, 'Q': 24, 'E': 25,'X':26}
inp=[]
for i in TokenListForParser:
    inp.append(mapper[i])




inp+='$'

class Stack:
    def __init__(self):
        self.s = []
        self.st = []

    def pop(self):
        return self.s.pop()

    def push(self, item):
        self.s.append(item)

    def sizeOfStack(self):
        return len(self.s)

    def peak(self):
        return self.s[len(self.s)-1]

    def printStack(self, nonterminals, terminals, t, string22, str1):
        for i in range(len(self.s)):
            if(self.s[i] in terminals):
                self.st.append(terminals[self.s[i]])
            elif(self.s[i] in nonterminals):
                self.st.append(nonterminals[self.s[i]])
            else:
                self.st.append(self.s[i])
        #print(self.st,end=" ")
        str2 = ' '.join(map(str, self.st))
        self.st = []
        t.add_row([str2, str1, string22])


# Parser Function
inpoot = []
s = Stack()

def foo(string):
    global index, inpIndex, inp, s, t, nonterminals, terminals, inpoot, temp

    if string[0] == 'r':  # do reducing
        temp1 = RulesTable[int(string[1:])]
        temp1 = temp1.split("->")
        g = temp1[1].split(" ")
        for i in range(len(g)*2):
            label = s.pop()
        num = s.peak()
        s.push(temp1[0])
        s.push(int(LR1Table[num][goto[temp1[0]]]))
        index = int(LR1Table[num][goto[temp1[0]]])
        # s.printStack(t,inp,string)
        # s.printStack(nonterminals,terminals,string)
        string22 = LR1Table[index][action[inp[inpIndex]]]
        # print(k)
        for l in range(inpIndex, len(inp)):
            inpoot.append(nonterminals[inp[l]])
        #print(string,end=" ")
        str1 = ' '.join(map(str, inpoot))
        #print(str1,end=" ")
        # print()
        inpoot = []
        s.printStack(nonterminals, terminals, t, string22, str1)
    else:  # do shifting

        s.push(inp[inpIndex])
        s.push(int(string[1:]))
        inpIndex += 1
        index = s.peak()
        string22 = LR1Table[index][action[inp[inpIndex]]]
        for l in range(inpIndex, len(inp)):
            inpoot.append(nonterminals[inp[l]])
        str1 = ""
        str1 = ' '.join(map(str, inpoot))
        inpoot = []
        s.printStack(nonterminals, terminals, t, string22, str1)

  # append dollar to the scanned input


LR1Table = []
#                   a  b  c  d  e  f  g  h  i  j  k  l  $  S' S  A  B  C  G  F  D  I  Z  Y  Q  E
LR1Table.append(['s2','','','','','','','','','','','','','','1','','','','','','','','','','','',''])#1
LR1Table.append(['','','','','','','','','','','','','accept','','','','','','','','','','','','','',''])#2
LR1Table.append(['','s3','','','','','','','','','','','','','','','','','','','','','','','','',''])#3
LR1Table.append(['','','','s6','','','','','','','','','','','','4','5','','','','','','','','','',''])#4
LR1Table.append(['','s7','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s8','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','s9','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','s10','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','s13','','','','','','','','','','','','11','12','','','','','','','',''])
LR1Table.append(['','r3','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','','','','','r1','','','','','','','','','','','','','',''])
LR1Table.append(['','s14','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s15','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s16','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s20','','','','','','','','','','','','','','17','18','','19','','',''])
LR1Table.append(['','','','','','s22','','','','','','','','','','','','','','21','','','','','','',''])
LR1Table.append(['','','','','','','','s23','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s24','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s25','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s26','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','s27','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s28','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s29','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s30','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','','','s32','','','','','','','','','','','','','','','31',''])
LR1Table.append(['','','','','','','s35','','','','','','','','','','','','','','','','33','','34','',''])
LR1Table.append(['','','','','','','s20','','','','','','','','','','','','','','','','','36','','',''])
LR1Table.append(['','','','','','','','','','s37','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','s22','','','','','','','','','','','','','','38','','','','','','',''])
LR1Table.append(['','','','','','','','s39','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','s40','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r2','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s41','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r7','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s42','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','s43','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s44','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r10','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r4','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s45','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s46','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','s47','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s35','','','','','','','','','','','','','','','','','','48','',''])
LR1Table.append(['','','','','s49','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s20','','','','','','','','','','','','','','','','','50','','',''])
LR1Table.append(['','r6','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r5','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','','s51','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r9','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r11','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s52','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','','','','','','s53','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s20','','','','','','','','','','','','','','','','','55','','','54'])
LR1Table.append(['','','','','','','','','','s56','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r8','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s57','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','s58','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','','','','','','s20','','','','','','','','','','','','','','','','','59','','',''])
LR1Table.append(['','','','s6','','','','','','','','','','','','','60','','','','','','','','','',''])
LR1Table.append(['','r13','','','','','','','','','','','','','','','','','','','','','','','','',''])
LR1Table.append(['','r12','','','','','','','','','','','','','','','','','','','','','','','','',''])


RulesTable=[]
RulesTable.append("S'->S")
RulesTable.append("S->a b A b c")
RulesTable.append("A->B b C b D b E")
RulesTable.append("B->d e")
RulesTable.append("C->G b F b F")
RulesTable.append("G->f g h g h g")
RulesTable.append("F->f g h g")
RulesTable.append("D->I b Z")
RulesTable.append("I->Y b Y b Y b X")
RulesTable.append("Z->Q b Q")
RulesTable.append("Y->g i j")
RulesTable.append("Q->g i e")
RulesTable.append("E->k g i j l j b B")
RulesTable.append("X->Y b Y")

s.push(0)

temp  = LR1Table[index][action[inp[inpIndex]]]
print()
print()
print("SEQUENTIAL PARSING STEPS:")
print()
t = tt.Texttable()
headings = ['Stack','Input','Action']
t.header(headings)

cd=[]
for l in range(0,len(inp)):
        cd.append(nonterminals[inp[l]])
cdstr = " "  
cdstr = ' '.join(map(str, cd)) 
t.add_row(['0',cdstr,temp])        

flag=0
#print(temp)
while(temp != "accept"):
 if temp == '':
    #print("ERROR")
    flag=1
    break
 foo(temp)
 temp  = LR1Table[index][action[inp[inpIndex]]]

s = t.draw()
print(s)   
#print(temp)
if(flag==1):
    print()
    print("ERROR!! The input doesnt satisfy the grammar")


