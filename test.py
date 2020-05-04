#praštevila do 200

def ali_je_prastevilo(n):
    deljitelji = 0
    for i in range(n):
        if n % (i + 1) == 0:
            deljitelji +=1
    return deljitelji == 2


for i in range(200):
    if ali_je_prastevilo(i+1):
        print(i+1)
