print("Program to find approximately value of log10(a)")
a = float(input("input the value of a : "))
U = a
L = 0
limit_error = 10e-10
x = (U+L)/2
cnt = 1
while abs(10**x-a)>limit_error :
    x = (U+L)/2
    print(f"Try : {cnt} |",f"log10({a}) =",x)
    if 10**x >= a :
        U = x
    else :
        L = x
    cnt+=1
print(f"Approximately value of log10({a}) is : "+str(x))