import pymysql
import pymysql.cursors
import os
import dotenv

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection =  pymysql.connect(
    host='localhost', #os.environ['MYSQL_HOST'],  # usando .env para as variables
    user='root',#os.environ['MYSQL_ROOT_PASSWORD'],
    password='root', # os.environ['MYSQL_ROOT_PASSWORD'],
    database='database', #os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor, # Mudando o cursor, muda o jeito que ele devolve a resposta no terminal, nesse caso, tudo que ele ler vai me retornar em forma de dicionario
    # Existe outro cursor, SSCursor e SSDictCursor que são unbuffered, eles não salvam na memória, parecido com generator
)

with connection:
    with connection.cursor() as cursor:
    # CRUD, CRIAMOS UMA TABELA(C)
    # Agora vamos fazer o READ(R)
    # Podemos selecionar itens especificos:
    # SELECT id, nome, idade,(nome das colunas)
    # ou TUDO(ALL)
    # SELECT * FROM {TABLE_NAME}
    # * -> TUDO(ALL)
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        # Quando vamos fazer a Leitura da Tabela
        # Não precisamos commitar
        # Commitar é meio que versionar alguma coisa
        # Se voce envia algo para a tabela e voce comita
        # Quando voce quiser enviar algo novamente e der erro
        # É possível dar um no-back nos envios para resolver o erro
        cursor.execute(sql)
        # fetchall -> Pega TODOS os valores da table
        # fetchmany -> Pega ALGUNS valores da table
        # fetchone -> Pega UM valor da table
        # data5 = tuple(cursor.fetchall())
        # print(data5)


        # Quando temos uma base de dados muito grande, jogar em numa variavel seria inviavel devido ao tamanho e quantidade da base de dados
        # Nesse caso usamos o "metodo" rolla(scroll) do cursor para ler cada
        # linha da tabela
        # Por padrão, ele vem no modo relativo, ou seja, eu determino a quantidade de linhas que ele ira rolar, pra cima ou para baixo
        # Mas tem o modo absoluto que eu escolho a linha que ele vai começar a ler, entao ele ira me mostrar desta linha ate o final da tabela
        cursor.scroll(6, 'absolute')
        for row in cursor.fetchall():
            # Dessa forma eu consigo desempacotar a lista
            print(row)
