#inverse function of log_n(x) is n^x
print("Program to find approximately value of log_n(a)")
a = float(input("input the value of a : "))
n = float(input("input the value of n : "))
U = a
L = 0
threshold = 10e-10
x = (U+L)/2
cnt = 1
while abs(n**x-a)>threshold :
    x = (U+L)/2
    print(f"Try : {cnt} |",f"log_{n}({a}) =",x)
    if n**x >= a :
        U = x
    else :
        L = x
    cnt+=1
print(f"Approximately value of log_{n}({a}) is : "+str(x))
