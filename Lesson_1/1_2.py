# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значения переменных, где "1" - истина, а "0" - ложь')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
print(not(x or y or z) == (not x) and (not y) and (not z))