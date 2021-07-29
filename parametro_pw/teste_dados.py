import csv
a ="C:\\Users\\JABANTU\\Desktop\\tudo\\New folder\\"
print ('Digite o serial')
s = input()
print ('Digite a OL')
ol = input()
print ('Digite a largura do pulso')
pw = input()
ende = a + s + '\PW'+pw+'\CH1\CH1_OL' + ol + '_PW'+pw+'.csv'

with open(ende,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    status = 0
    reprovados = {}
    for line in csv_reader:
        teste = line [17]
        print(teste)
        print(line[17])
        f = float(teste)
        if f > 2.5:
            status = 1
            reprovados.append = f
    if status == 0:
        
        print("aprovado")
    else:
        print("reprovado")
