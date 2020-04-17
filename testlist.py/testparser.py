class Stack:
	def __init__(self):
		self.s = [] 
	def pop(self):
		return self.s.pop()
	def push(self, item):
		self.s.append(item)
	def sizeOfStack(self):
		return len(self.s)
	def peak(self):
		return self.s[len(self.s)-1]
	def printStack(self):
		for i in range(len(self.s)):
			print(self.s[i])	
def foo(string ):
	global  index , inpIndex,inp,s,nodeNum,flage

	try:
		#print(string)
		index = int(string)
	except:
		if string[0] == 'r': # do reducing 
			temp = RulesTable[int(string[1:])]
			temp = temp.split("->")
			g = temp[1].split(" ")
			for i in range( len(g)*2 ):
				label = s.pop()
			num  = s.peak()
			s.push(temp[0])
			s.push(LR1Table[num][goto[temp[0]]])
			index = LR1Table[num][goto[temp[0]]]
		else: # do shifting 

			s.push(inp[inpIndex])
			s.push(int(string[1:]))
			inpIndex+=1
			index = s.peak()



index = 0
inpIndex = 0  # input pointer 
nodeNum = 0  # number of node for graphviz 
flage =1

s = Stack()



inp = input(" enter taken ")
inp += " $"
inp = inp.split(' ')

terminals = ['+','ID']
nonterminals = ['S\'','S']

action  = {'+':0 ,'ID':1, '$':2}
goto ={'S\'':3 , 'S':4}

#rl(1) table 
LR1Table = []
LR1Table.append(['','s2','','',1])
LR1Table.append(['s3','','acc','',''])
LR1Table.append(['r2','','r2','',''])
LR1Table.append(['','s2','','',4])
LR1Table.append(['s3','','r1','',''])

#rules table
RulesTable = [] 
RulesTable.append("S'->S")
RulesTable.append("S->S + S")
RulesTable.append("S->ID")


s.push(0)
temp  = LR1Table[index][action[inp[inpIndex]]]

while(temp != "acc"):
	if temp == '':
		print("error")
		break
	foo(temp)
	temp  = LR1Table[index][action[inp[inpIndex]]]


