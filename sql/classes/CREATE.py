# PyMySQL - um cliente MySQL feito em Python puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql
# GitHub: https://github.com/PyMySQL/PyMySQL
# MariaDB é um fork de MySQL, as mesmas QUERYS do MySQL
# servem também para MariaDB
# PyMySQL é feito em Python Puro então
# é possível usar o Context Manager para fazer QUERYS
import pymysql
import pymysql.cursors
import dotenv
import os

# Pega a variável de ambiente
dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host='localhost', #os.environ['MYSQL_HOST'],  # usando .env para as variables
    user='root',#os.environ['MYSQL_ROOT_PASSWORD'],
    password='root', # os.environ['MYSQL_ROOT_PASSWORD'],
    database='database', #os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor,
)
# Forma normal de fazer QUERYS
# cursor = connection.cursor()
# cursor.close()
# connection.close()
# Fazendo QUERYS com Context Manager
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # CUIDADO: TRUNCATE LIMPA A TABELA
        # EM PRODUÇÃO TER UM BACKUP DA TABLE SE FOR USAR ESSE COMANDO
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    # Começo a manipular dados a partir daqui
    # Não é uma boa prática mandar os valores na QUERY SQL
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '  # Nome(%s): PlaceHolder
        )
        # PlaceHolder (%(name)s, %(ge)s)'
        # Os nomes de dentro do place holder indícam as chaves dos dicionarios,
        # isso influencia na hora da execução
        # Mas, quando é uma lista ou uma tupla, apenas deixar o %s, indica:
        # Inserir na ordem do iterável
        data6 = (
            {"name": "Le", "age": 27, },
            {"name": "Robb", "age": 20, },
            {"name": "Jack", "age": 19, },
            {"name": "Rat", "age": 12, },
            {"name": "Buddy", "age": 100, },
            {"name": "Bro", "age": 43, },
            {"name": "Ouyeah", "age": 18, },
            {"name": "Oumagod", "age": 19, },
            {"name": "Farros", "age": 12, },
            {"name": "Cebolao", "age": 8, },
        )

        # data2 = {
        #     "name": "Robb",
        #     "age": 69,
        # }

        # data4 = (
        #     ("Siri", 22 ),
        #     ("Cortana", 15 ),
        # )

        # result = cursor.execute(sql, data)
        # Para usar o executemany, usar um iterável -> Tuple, list,
        # dictionaries
        result = cursor.executemany(sql, data6)
        # result = cursor.executemany(sql, data4)
    connection.commit()
