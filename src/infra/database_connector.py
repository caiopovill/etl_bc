import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


con = {'host':os.environ.get('HOSTNAME'),
       'database':os.environ.get('DATABASE'),
       'user':os.environ.get('USERNAME'),
       'password':os.environ.get('PASSWORD'),
       'port':os.environ.get('PORT')}

class DatabaseConnector:

    connection = None

    @classmethod
    def connect(cls):
        df_connection = psycopg2.connect("""dbname='postgres'
                                            user='postgres'
                                            host='localhost'
                                            password='postgres'"""
        )
        cls.connection = df_connection
