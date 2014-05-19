
tam=1001
i=1
xOrig =(tam-1)/2
yOrig=(tam-1)/2
x=xOrig
y=yOrig
dir=0
lado=1
cnt=lado
tamTotal=tam*tam
suma=0
while i<=tamTotal:
    if abs (x-xOrig) == abs(y-yOrig):
        suma+=i
    if dir == 0:
        x+=1
    elif dir == 1:
        y+=1
    elif dir == 2:
        x-=1
    elif dir == 3:
        y-=1
    cnt-=1
    if cnt<=0:
        if dir%2==1:
            lado+=1
        cnt=lado
        dir = (dir+1)%4
    i+=1
print suma
