arquivo = open('teste.txt', 'a')
for i in range(1,11):
    arquivo.write(f'Opção: {i}!=i+1\n')
arquivo.write('Oitava execução!\n')
arquivo.close()

arquivo2 = open('teste.txt', 'r')
conteudo = arquivo2.read()
print(conteudo)
arquivo2.close()
