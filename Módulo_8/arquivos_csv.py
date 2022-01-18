from csv import DictReader,DictWriter


with open('pessoas.csv','w',newline='',encoding='utf-8') as arquivo:
    cabecalho= ['nome','idade','altura']
    csv_writter = DictWriter(arquivo, cabecalho)
    csv_writter.writeheader()
    csv_writter.writerow({
        'nome': 'Mark',
        'idade': '25',
        'altura': '170',
    }),
    csv_writter.writerow({
        'nome': 'Carol',
        'idade': '19',
        'altura': '160',
    }),
    csv_writter.writerow({
        'nome': 'Robert',
        'idade': '65',
        'altura': '175',
    }),

with open('pessoas.csv','r',newline='',encoding='utf-8') as arquivo_original:
    dados_originais=DictReader(arquivo_original)
    lista=list(dados_originais)
    with open('pessoas_v2.csv','w',newline='',encoding='utf-8') as arquivo_novo:
        cabecalho= ['nome','idade','altura']
        csv_writter=DictWriter(arquivo_novo, cabecalho)
        csv_writter.writeheader()
        for listas in lista:
            csv_writter.writerow({
                'nome': listas['nome'],
                'idade': listas['idade'],
                'altura': listas['altura'] + 'cm',
            })
            
            
            
    