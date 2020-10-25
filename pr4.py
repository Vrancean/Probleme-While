x=eval(input("dati un numar:"))
s=0
p=1
nr=1
while x>=nr:
    s+=nr
    p*=nr
    nr+=1 

print("s=",s)
print("p=",p)
print("media aritmetica=",s/x)