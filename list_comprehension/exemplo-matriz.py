mat = []
for j in range(3):
    linha = []
    for i in range(4):
        linha.append(i+1+j*4)
    mat.append(linha)
print(mat)

mat2 = [[i+1+j*4 for i in range(4)] for j in range(3)]
print(mat2)