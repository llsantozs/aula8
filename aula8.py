
# # 01
nmr = float(input('Digite um numero aleatorio:'))

if nmr >= 1:
     print('positivo', nmr)

elif nmr <= 0:
     print('negativo', nmr)

else:
     print('zero', nmr)

# # 02
nmr2 = float(input('Digite sua idade: '))

if nmr2 >= 16:
   print('Pode votar!')

else:
   print('Ainda não pode votar! :(')

# # 03
nmr3 = float(input('Digite um numero: '))

if nmr3 % 2 == 0:
     print('é par')
else:
     print('é impar')

# # 04
print ('Vamos criar um triangulo!')
nmr4 = input('Digite um numero: ')
nmr5 = input('Digite um numero: ')
nmr6 = input('Digite um numero: ')

if nmr4 == nmr5 == nmr6:
    print('esse triangulo é equilatero!')

elif nmr4 == nmr5 or nmr4 == nmr6:
     print('esse triangulo é isosceles')

else:
     print('esse triangulo é escaleno')
    
# 05
nmr7 = int(input('Digite um numero múltiplo de 5 e 7: '))

if nmr7 % 5 == 0 or nmr7 % 7 == 0:
     print('Parabens!')

else:
     print('tente novamente')

# 06
nmr8 = float(input('Digite um numero aleatorio:'))
if nmr8 >= 10: 
     print('Parabens')
else:
     print('tente novamente')

# 07

nmr8 = int(input('Digite um numero múltiplo de 5 e 3: '))

if nmr8 % 5 == 0 and nmr8 % 3 == 0:
     print('Parabens!')

else:
    print('tente novamente')
