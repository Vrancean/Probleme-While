nr=0
sp=0
np=0
sn=0
ng=0
mp=0
mn=0
n=1
while nr<=12 :
    n=eval(input('dati un numar:'))
    nr=nr+1
    if n>=0:
        np=np+1
        sp+=n
    else:
        ng=ng+1
        sn+=n

mp=sp/np
print("media pozitiva =",round(mp,2))
mn=sn/ng
print("media negativa =",round(mn,2))
