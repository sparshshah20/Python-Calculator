def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "cannot be divided by zero"
    return a/b

a=float(input("enter the first number"))
b=float(input("enter the second number"))

print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice=input("enter the number of your choice(1-4):")

if choice =="1":
    print("result=",add(a,b))

elif choice=="2":
    print("result=",subtract(a,b))

elif choice=="3":
    print("result=",multiply(a,b))

elif choice=="4":
    print("result=",divide(a,b))

else :
    print("invalid choice")