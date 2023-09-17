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
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id = %s'
        )
        # Se não colocar um commit, ele mostra que alterou na tabela
        # mas na verdade não aconteceu nada, pois o commit altera e salva de verdade
        #
        cursor.execute(sql, ('Henrique', 30, 4))
        connection.commit()