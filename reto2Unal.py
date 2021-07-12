pedro = input()
pablo = input()
llegada = input()

pedroCont = 0
pabloCont = 0
for c in llegada:
    for i in pedro:
        if c == i:
            pedroCont = pedroCont + 1
    for j in pablo:
        if c == j:
            pabloCont = pabloCont + 1
    if pedroCont > pabloCont:
        print('x',end="")
    elif pabloCont > pedroCont:
        print('y',end="")
    else:
        print('z',end="")

