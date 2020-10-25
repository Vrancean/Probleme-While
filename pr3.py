s=0
x=1
while x%2!=0 and x%3!=0 :
    x=eval(input("dati un numar:"))
    while x%2==0:
        s+=x
        x=eval(input("dati un numar:"))

print("s=",s)
    