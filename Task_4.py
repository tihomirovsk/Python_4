from random import randint
max_val=100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(poly)