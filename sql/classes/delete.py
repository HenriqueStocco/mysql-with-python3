import pymysql
import pymysql.cursors
import os
import dotenv

dotenv.load_dotenv()
TABLE_NAME = 'customers'
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='database',
    charset='utf8mb4',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id <= %s'
        )
        # Sempre Passar o WHERE para DELETE, se não ele apaga TODOS os dados
        # Esse print mostra a quantidade de itens afetados
        # SEMPRE ter um BACKUP da base de dados antes de sair deletando as coisas ou dando update
        print(cursor.execute(sql, (2,)))
        # cursor.execute(sql)
        connection.commit()