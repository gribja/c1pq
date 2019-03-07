
def fac(n):
    f = 1
    for i in range(2,n+1):
        f*=i
    return f

xs = [10,20,30,40,50]
ys = [46,66,81,93,101]

def u_dec(u,n):
    x_temp = u
    for i in range(0,n):
        x_temp *= (u-i)
        return x_temp


def forward(x,xp,yp):
    n = len(xp)  
    y_diff = [[0]*n for i in range(n)]
    
    for i in range(0,n):
        y_diff[i][0] = yp[i]
    
    for i in range(1,n):
        for j in range(0,n-i):
            y_diff[j][i] = y_diff[j+1][i-1] - y_diff[j][i-1]

    print(y_diff)  

    sum = y_diff[0][0] 
    
    u = (x - xp[0])/(xp[1]-xp[0]) 

    for i in range(1,n):
        sum += (u_dec(u,i)*y_diff[0][i])/fac(i)  

    return sum

print(xs)
print(ys)
print(forward(15,xs,ys)) 
