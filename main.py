n1 = int(input('1 cilv. masa(kg) : '))

n2 = int(input('2 cilv. masa(kg) : '))

summa = n1 + n2

print('Sum =', summa)

n3 = [n1, n2]

print(sum(n3) / len(n3))

if summa >= 300:

print("nevar braukt lifta")

else:

print("var braukt lifta")