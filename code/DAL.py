import psycopg2 # PostgreSQL database adapter for Python
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import configparser # to work with the configuration file

config = configparser.ConfigParser()
config.read('dwh.cfg') # edit this file to include your own values.

# read config values
HOST=config['database']['HOST']
DB_NAME=config['database']['DB_NAME']
DB_USER=config['database']['DB_USER']
DB_PASSWORD=config['database']['DB_PASSWORD']
csv_path=config['other']['csv_path']

# database access layer
def create_database():
    """
    - Drop and Creates the Database
    """    
    # connect to default database
    conn = psycopg2.connect("host={} \
                             user={} \
                             password={}".format(HOST,
                                                 DB_USER,
                                                 DB_PASSWORD))
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    #cur.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))
    
    cur.execute("CREATE DATABASE {} WITH ENCODING 'utf8' \
                TEMPLATE template0".format(DB_NAME))

    # close connection to default database
    cur.close()
    conn.close()  
    
    print('Database Creating')
    
def connect_database():
    """
    - Connect and returns the connection 
        and cursor for database
    """
    
    # connect to database
    
    conn = psycopg2.connect("host={}  \
                            dbname={} \
                            user={} \
                            password={}".format(HOST,
                                                DB_NAME,
                                                DB_USER,
                                                DB_PASSWORD))
    
    conn.set_session(autocommit=True)
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur = conn.cursor()
        
    return cur, conn
