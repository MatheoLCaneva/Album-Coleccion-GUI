from ast import literal_eval

file = open("figuritas_coleccion.txt", "r+")

content = file.read()
content = literal_eval(content)

obj = {"nombre": "juan", "apellido": "lopez" }
content.append(obj)

print(content)

for i in range(0, len(content)):
    content[i] = str(content[i])

a = "[{}]".format(' '.join(content))

print(a)
    


# file.write(content)
# file.close()
