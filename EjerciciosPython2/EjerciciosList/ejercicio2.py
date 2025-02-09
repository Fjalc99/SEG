#Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.

for i in range(1,1000):
    if '3' in str(i):
        print(i)