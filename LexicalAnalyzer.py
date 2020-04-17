# Token Defs
operators = {':=': 'Assignment Operator'}
optr_keys = operators.keys()
datatype = {'INTEGER': 'Integer datatype',
            'STRING': 'String datatype', 'REAL': 'Real datatype'}
datatype_keys = datatype.keys()
separator = {",": "Comma"}
separator_keys = separator.keys()
keyword = {'return': 'keyword that returns a value from a block',
           'BEGIN': 'Start of code segment', 'END': 'End of Code segment', 'FOR': 'For Loop', 'TO': 'Range keyword', 'PRINT': 'Print Statement'}
keyword_keys = keyword.keys()
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# To Generate a list for all the tokens

f = open('InputProg.txt', 'r', encoding="utf8")
i = f.read()
flag = False
newList = []
newToken = ""
program = i.split('\n')
tokenList = []
for line in program:
    tokens = line.split(' ')
    tokenList += tokens
for token in tokenList:
    if token[0] == '\"' and token[len(token)-1] == '\"':
        newList.append(token)
    elif token[0] == '\"':
        newToken += token
        flag = True
    elif token[len(token)-1] == '\"':
        newToken += " "+token
        newList.append(newToken)
        flag = False
        newToken = ""
    elif flag == True:
        newToken += " "+token
    elif flag == False:
        newList.append(token)
for i in [1, 4, 11, 16, 21, 25, 29, 33, 37, 41, 45, 49, 56, 59]:
    newList.insert(i, '\n')


# Scan each token in List and create a new List for Token Definition

print("---------------Lexical Analysis-----------------")
TokenListForParser = []
for token in newList:
    if token in optr_keys:
        print("Operator : ", token + " -->", operators[token])
        TokenListForParser.append('equals')
    elif token in datatype_keys:
        print("Datatype : ", token + " -->", datatype[token])
        TokenListForParser.append('datatype')
    elif token in keyword_keys:
        print("Keyword : ", token+" -->", keyword[token])
        TokenListForParser.append(token.lower())
    elif token.isidentifier():
        print("Identifier : ", token + " --> Identifier variable")
        TokenListForParser.append('id')
    elif token[0] == '\"':
        print("String :", token+"--> Explicit String Values")
        TokenListForParser.append('string')
    elif token in numerals or 'E' in token or '.' in token:
        print("Number :", token+" -->Numeric Value")
        TokenListForParser.append('number')
    elif token == ',':
        print('Separator :', token+' -->Separator operator')
        TokenListForParser.append('comma')
    elif token == '\n':
        print('NewLine: \\n -->Newline')
        TokenListForParser.append('newline')


print("---------------Lexical Analysis Complete-----------------")
print(TokenListForParser)
f.close()
