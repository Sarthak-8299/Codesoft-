print('two number below : ')
a=int(input('enter a first number'))
b=int(input('enter a second number'))
ch=0
while ch<5:
    print('calculator menu')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    print('5.Exit')
    ch=int(input('enter your choice'))
    if ch==1:
        c=a+b 
        print('sum:',c)
    elif ch==2:
        c=a-b
        print('subtract',c) 
    elif ch==3:
        c=a*b
        print('multiply',c)
    elif ch==4:
        c=a/b
        print('divide',c)
    elif ch==5:
        break
    else:
        print('INVALID CHOICE') 
