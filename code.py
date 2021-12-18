
print("Welcome To Mr India's Calculator .")
print(" If You Want To do any subtraction ,Division ,Multiplication This Calculator helps you")
# code for addition function
def add(a,b):
    result=a+b
    print("Answer:-",result)
#code for subtraction function
def sub(a,b):
    result=a-b
    print("Answer:-",result)
#code for multiplication Function
def mul(a,b):
    result=a*b
    print("Answer:-",result)
#code for division function
def div(a,b):
    result=a/b
    print("Answer:-",result)
# THis is only text to show 
a=int(input("Enter The First Number:- "))
b=int(input("Enter The Second Number:- "))

# This is only for the operator text to show
op =input("Enter The Operator:- ")
# This is the if function 
if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid Opera")

#Now your calculator is ready 
# Now we test the calculator
# To test the calculater in coder editor we have to do click on this button 
 
