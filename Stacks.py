print("1.Push\n2.pop\n3.display")
maxlen=5
Stack=[]
def push(val):
    if(len(Stack)>=maxlen):
        print("Stack over flow")
        exit
    else:
        Stack.append(val)
def rem():
    if(len(Stack)<=0):
        print("Stack underflow")
    else:
        print("The removed element is", Stack[-1])
        Stack.pop()
def display():
    print(Stack[::-1])

def func():
    CH=int(int(input("Enter your choice: ")))
    if(CH==1):
        val=int(input())
        push(val)
        func()
    elif(CH==2):
        rem()
        func()
    elif(CH==3):
        display()
        func()
    elif(CH==4):
        print("Thank you")
        exit
    else:
        print("Invalid input")
        func()

func()
