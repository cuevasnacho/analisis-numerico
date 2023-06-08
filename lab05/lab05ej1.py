# regla del trapecio
def trapecio(fun,a,b,N):
    h = (b-a)/N
    sumatxj = 0
    for j in range(1,N):
        sumatxj += fun(a+j*h)
    S = (h*(fun(a)+2*sumatxj+fun(b)))/2

    return S

# regla del punto medio
def punto_medio(fun,a,b,N):
    h = (b-a)/(N+2)
    sumatxj = 0
    cota = int(N/2+1)
    for j in range(cota):
        sumatxj += fun(a+(2*j+1)*h)
    S = 2*h*sumatxj

    return S

# regla de simpson
def simpson(fun,a,b,N):
    h = (b-a)/(2*N)
    sx0 = fun(a) + fun(b)
    sx1 = 0
    sx2 = 0
    x = a
    for j in range(1,2*N):
        x = x+h
        if (j%2==0):
            sx2 += fun(x)
        else:
            sx1 += fun(x)
    S = (sx0 + 2*sx2 + 4*sx1)*(h/3)
    
    return S

# fun: R->R; a,b extremos; N cantidad de subintervalos; regla string (pm, trapecio, simpson)
def intenumcomp(fun,a,b,N,regla):
    if (regla == "trapecio"):
        S = trapecio(fun,a,b,N)
    elif (regla == "pm"):
        S = punto_medio(fun,a,b,N)
    elif (regla == "simpson"):
        S = simpson(fun,a,b,N)
    else:
        print("Intente otra vez")
    
    return S