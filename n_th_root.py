cnt = 1
# inverse function of nth_root(x) is x^n
# don't support negative value a
# support case n>0 and n<1
print("Program to find approximately value of nth_root(a)")
a = float(input("input the value of a : "))
n = float(input("inout the value of n : "))
U = a
if a<1 :
    U = 1
if n<1 :
    U = 10e10
L = 0
limit_error = 10e-10
x = (U+L)/2
while abs(x**n-a)>limit_error :
    x = (U+L)/2
    print(f"Try : {cnt} |",f"{n}th_root({a}) =",x)
    if x**n >= a :
        U = x
    else :
        L = x
    cnt+=1
print(f"Approximately value of {n}th_root({a}) is : "+str(x))
