import numpy as np

n = int(input("n="))
a = np.zeros(n-1)


for i in range (0,n-1):
    a[i] = i+2

print("РЕШЕТО ЭРАТОСФЕНА")
for i in range (0,n-1):
    for j in range (i+1,n-1):
        if (a[i]!=-1):
            if (a[j]%a[i]==0):
                a[j] = -1

for i in range (0,n-1):
   if (a[i]!=-1):print(a[i])
