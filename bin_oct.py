a=int(input("x: "))
a=bin(a).replace("0b","")
b=int(input("y: "))
b=oct(b).replace("0o","")
print(a,",",b)