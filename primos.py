from mpi4py import MPI
import math as m
import time
import sys
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
termino = False

def isPrime(n):
    sw = True
    if(n < 2):
        return False
    j = 2
    while(j <= m.sqrt(n) and sw):
        if n % j == 0:
            sw = False
        j += 1
    return sw

prim=0
i = rank*size+1
if rank==0:
    prim=1
while not(termino):
    k = int(sys.argv[1])
    h=size
    const=(size-1)*size
    ti=time.time()
    while(i <= k):
        if i + size >k:
            h= -i+k+1
        for x in range(0,h):
            # print(i,"rank:",rank)
            prim = prim+isPrime(i)
            i = i+ 1
        i=const+i
    tf=time.time()
    termino = True
prim=comm.gather(prim, root=0)
t=comm.gather(tf-ti, root=0)

if (rank == 0):
    print('De 1 a ',k,' Tiene ',sum(prim),' numeros Primos en ',max(t))