exp=input("enter expression for evaluation") 
#validating entered string and generating infix from given arithmetic expression
bracket=0
operand =0
num=""
infix=""
maps={}
key=ord('a')
for i,letter in enumerate(exp): 
    if letter not in ['+','-','*','/','^','(',')','{','}','[',']']:
        num+=letter
        operand+=1
    else:
        if letter in ['(','{','[']:
            infix+=letter
            bracket+=1
            if i==len(exp)-1:
                raise ValueError("Entered Expression is invalid.")
        else:
            flag=True
            if letter in [')',']','}']:
                bracket-=1
                if i==0:
                    raise ValueError("Entered Expression is invalid.")
            if letter in ['+','-','*','/','^']:
                if i==0 or i==len(exp)-1:
                    raise ValueError("Entered Expression is invalid.")
                if exp[i-1] in ['+','-','*','/','^','(','{','[']:
                    raise ValueError("Entered Expression is invalid.")
                if exp[i+1] in ['+','-','*','/','^',')',']','}']:
                    raise ValueError("Entered Expression is invalid.")
            if not infix and letter in ['+','-','*','/','^']:
                maps[chr(key)]=num
                num=""
                infix+=chr(key)
                infix+=letter 
                flag=False
                key+=1
            if infix[-1] not in[')',']','}'] and flag:
                maps[chr(key)]=num
                num=""
                infix+=chr(key) 
                key+=1
            if flag:
                infix+=letter
    print(f"current letter is {letter} and expression is {infix}")
if bracket or not operand:
    raise ValueError("Entered Expression is invalid.")
if num:
    maps[chr(key)]=num
    num=""
    infix+=chr(key) 
    key+=1 
print(maps)
print(infix)
# converting the infix expression to postfix one
expression=infix
postfix=""
stack=[]
exponent=0
precedence={'-':0,'+':1,'*':2,'/':2,'^':3}
for symbol in expression:
    #check if scanned symbol is an operator
    if symbol in ['+', '-','/','*','(',')','{','}','[',']']:
        if  symbol== '*':
            exponent+=1 #to consider two consecutive multplication symbols as exponent operator ie replace ** by ^
            if exponent==2:
                exponent-=2
                stack.pop()
                symbol='^'
        #checking precedence
        if symbol not in [')','(','[',']','{','}'] and len(stack) >=1 and stack[-1] not in ['(','[','{']:
            if precedence[symbol]<precedence[stack[-1]]:
                while stack[-1] not in ['(','[','{'] or stack:
                    postfix+=stack.pop() #adding operator to target string to maintain precedence
                    if not stack:
                        break
                    if stack[-1] in ['(','[','{'] :
                        break
        #handling cases when there are multiple multiplications symbols but they are not consecutive
        if symbol != '*' and exponent==1:
            exponent=0
        stack.append(symbol) #adding operator to the stack
        #poping items in case of hitting a closing bracket
        if symbol in [')',']','}']:
            stack.pop() 
            while stack[-1] not in ['(','{','[']:
                postfix+=stack.pop() #adding operator to target string to maintain precedence
            stack.pop()
    #if scanned symbol is an operand add it to the target string 
    else: 
        postfix+=symbol
while stack:
    postfix+=stack.pop() 
print(postfix)
stack=[]
def evaluator(operand2,operand1,operation):
    if operation=='-':
        return operand1-operand2
    elif operation=='+':
        return operand1+operand2
    elif operation=='*':
        return operand1*operand2
    elif operation=='/':
        return operand1/operand2
    else:
        return operand1**operand2
for symbol in postfix:
    if symbol not in ["+","-","*","/","^"]:
        stack.append(symbol)
    else:
        if type(stack[-1]) == str and type(stack[-2]) == str:
            stack.append(evaluator(float(maps[stack.pop()]),float(maps[stack.pop()]),symbol))
        elif type(stack[-1])== str:
            stack.append(evaluator(float(maps[stack.pop()]),stack.pop(),symbol))
        elif type(stack[-2])== str:
            stack.append(evaluator(stack.pop(),float(maps[stack.pop()]),symbol))
        else:
            stack.append(evaluator(stack.pop(),stack.pop(),symbol))
    print(stack)
print(stack[0])