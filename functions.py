def hello():
    print("Hello world")
hello()

# Solicitando valor
def sumar():
    edad = input('Cual es tu edad?: ')
    res = int(edad) + 1
    print(res)
sumar()

# Retonando valor
def add(num1, num2):
    return num1 + num2
print(add(10,30))

# Function lambda
lam = lambda num1, num2: 
    num1+num2
print(lam(10,20))