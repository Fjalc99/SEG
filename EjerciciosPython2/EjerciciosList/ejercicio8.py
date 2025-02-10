#Dado numbers = range(20), se genera una lista que contiene la palabra "par" si un número en los números es par, 
# y  la palabra "impar" si el número es impar. El resultado se vería así: "impar", "impar", "par".


def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numbers = range(20)
for i in numbers:
    print(par_o_impar(i))