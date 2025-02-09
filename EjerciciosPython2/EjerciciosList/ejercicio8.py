#Dado numbers = range(20), se genera una lista que contiene la palabra "par" si un número en los números es par, 
# y  la palabra "impar" si el número es impar. El resultado se vería así: "impar", "impar", "par".



numbers = range(20)
for i in numbers:
    if i % 2 == 0:
        print("par")
    else:
        print("impar")

