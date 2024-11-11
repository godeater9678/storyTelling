import mysql.connector
from com.switchwon.config.logger_config import get_logger
from com.switchwon.config.profile import active_profile
from mysql.connector import Error
from sqlalchemy import create_engine

# 로거 설정
logger = get_logger()
profile = active_profile()


def __get_database_connection(connection_name: str):
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host=profile['database'][connection_name]['host'],
            database=profile['database'][connection_name]['database'],
            user=profile['database'][connection_name]['userid'],
            password=profile['database'][connection_name]['password'],
            port=profile['database'][connection_name]['port'],
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.close()
            # connection.close()
            # print("MySQL connection is closed")
            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)


def get_alchemy_connection_exchange():
    connection_name = 'database_exchange'
    host = profile['database'][connection_name]['host']
    database = profile['database'][connection_name]['database']
    user = profile['database'][connection_name]['userid']
    password = profile['database'][connection_name]['password']
    port = profile['database'][connection_name]['port']
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine


def get_database_connection_exchange():
    return __get_database_connection('database_exchange')
