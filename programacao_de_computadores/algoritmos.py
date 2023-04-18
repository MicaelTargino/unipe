def mediaAritmetica(x,y,z):
    r = (int(x) + int(y) + int(z))/3
    if r >= 7:
        print('aprovado')
    else:
        print('reprovado')    
    print(r)


xx = input('Num1:')    
yy = input('Num2:')    
zz = input('Num3:')

mediaAritmetica(xx,yy,zz)

