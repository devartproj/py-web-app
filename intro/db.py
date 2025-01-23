import pymysql

db_ini = {
    'host': 'localhost',
    'port': 3306,
    'user': 'py9_user',
    'password': 'pass', 
    'database': 'py9',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci'
}
db_connection = None

def connect_db (): 
    global db_connection
    try:
        print('Connecting to database...')
        db_connection = pymysql.connect(**db_ini)
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
    else:
        print('Connection successful')


def show_databases () :
    global db_connection
    sql = "SHOW DATABASES"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
            column_names = [desc[0] for desc in cursor.description]
            print(column_names)
            for row in cursor:
                print(row)
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return
    

def create_users () :
    global db_connection
    sql = """CREATE TABLE users (
        `id`        BIGINT UNSIGNED PRIMARY KEY  DEFAULT (UUID_SHORT()),
        `login`     VARCHAR(32)  NOT NULL  UNIQUE,
        `password`  CHAR(32)    NOT NULL,
        `avatar`    VARCHAR(256)  NULL
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci
    """
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql)
    except pymysql.MySQLError as err:
        print(err)
        return
    else:
        print('CREATE TABLE users -- OK')


def main() -> None:
    connect_db()
    create_users()
    
if __name__ == '__main__':
    main()
