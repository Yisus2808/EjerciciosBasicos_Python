myStr = "hello world"

print("Otro txt " + myStr )
print(f"Otro txt {myStr}")

# Sus metodos
print(dir(myStr))

# Uso 
print(myStr.replace('hello', 'bye').upper())
print(myStr.startswith('hello'))
print(myStr.endswith('bye'))
print(myStr.count('l'))
print(myStr.split())
print(myStr.find('o'))
print(len(myStr))