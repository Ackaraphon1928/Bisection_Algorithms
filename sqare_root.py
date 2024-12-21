print("Program to find approximately value of sqrt(a)")
a = float(input("input the value of a : "))
U = a
L = 0
limit_error = 10e-10
x = (U+L)/2
cnt = 1
# inverse function of sqrt(x) is x^2
while abs(x**2-a)>limit_error :
    x = (U+L)/2
    print(f"Try : {cnt} |",f"sqrt({a}) =",x)
    if x**2 >= a :
        U = x
    else :
        L = x
    cnt+=1
print(f"Approximately value of sqrt({a}) is : "+str(x))
