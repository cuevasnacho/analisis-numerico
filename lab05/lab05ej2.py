# error trapecio
def trapecio_err(n):
    return (1/(12*n**2))

# error simpson
def simpson_err(n):
    return (1/(180*n**4))

# error punto medio
def punto_medio_err(n):
    return (1/(6*(n+2)**2))

# pruebas
#print("trapecio: ",trapecio_err(4),trapecio_err(10),trapecio_err(20))
#print("simpson: ",simpson_err(4),simpson_err(10),simpson_err(20))
#print("pm: ",punto_medio_err(4),punto_medio_err(10),punto_medio_err(20))