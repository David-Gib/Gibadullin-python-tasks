#Begin33 Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.
X = float(input())
A = float(input())
Y = float(input())
price_1 = A / X
price_Y = price_1 * Y
print("Begin33:", price_1, price_Y)