print("Program to find approximately value of a")
a = int(input("input the value of a : "))
U = a
L = 0
limit_error = 10e-10
x = (U+L)/2.0
while abs(x**2-a)>limit_error :
    print("value : ",x)
    x = (U+L)/2
    if x**2 >= a :
        U = x
    else :
        L = x
print(f"Approximately value of sqrt({a}) is : "+str(x))
    