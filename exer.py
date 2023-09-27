#task22
n = int(input('Введите число: '))
m = int(input('Введите число: '))
fun1 = set(input('Введите числа через пробел: ').split()[:n])
fun2 = set(input('Введите числа через пробел: ').split()[:m])
lists = list()
fun3 = fun1.intersection(fun2)
fun3 = sorted(list(fun3))
print(fun3)

#task24

n = int(input('Введите количество кустов: '))
stra = list()
for i in range(n):
    a = int(input('Введите количество ягод на кусте: '))
    stra.append(a)

stra_count = list()
for i in range(len(stra)):
       stra_count.append(stra[i-2] + stra[i-1] + stra[i])
print(max(stra_count))