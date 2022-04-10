print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter Choice: "))
if ch==1:
    a=int(input("Enter 1st Number:"))
    b=int(input("Enter 2nd Number:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter 1st Number::"))
    b=int(input("Enter 2nd Number:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter 1st Number::"))
    b=int(input("Enter 2nd Number:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter 1st Number::"))
    b=int(input("Enter 2nd Number:"))
    if(b!=0):
        c=a/b
        print("Quotient = ",c)
    else:
        print("Value is Infinity.")
else:
    print("Invalid Choice")
