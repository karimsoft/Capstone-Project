import os
import psycopg2 # PostgreSQL database adapter for Python
import pandas as pd
import configparser # to work with the configuration file
import DAL as dal 

# user-defined functions
def exec_sql(ssql): 
    """
    Connect to postgres database, execute query,close connection.
    DDL,DML
    """
    
    cur, conn= dal.connect_database()
       
    try:
        cur.execute(ssql)
        
        conn.commit()
        
        cur.close
        conn.close
    except Exception as e:
        print('Error: ',e)
        
def select_sql(ssql,nlimit =10): 
    """
    Connect to postgres database, execute query,close connection.
    DDL,DML
    """        
    cur, conn= dal.connect_database()
       
    try:
        
        if nlimit>0:
            ssql=ssql+" limit ".format(nlimit)
            
        df = pd.read_sql(ssql, conn)
        
        return df        
        
    except Exception as e:
        print('Error: ',e)    
    finally:        
        cur.close()
        conn.close()        

def select_schema(table_name): 
    """
    view the schema of a table
    """       
    
    cur, conn= dal.onnect_database()
    
    try:    
        df = pd.read_sql(f"select column_name, data_type, character_maximum_length \
                            from INFORMATION_SCHEMA.COLUMNS where table_name ='{table_name}';", conn)                
        return df        
        
    except Exception as e:
        print('Error: ',e)             
    finally:
        cur.close()
        conn.close()        

def create_schema_from_csv(file_name,table_name,drop_table=False, sep=","):
    """
    create table from csv file in databse table
    """     
    cur, conn= dal.connect_database()
    col_list=""
    try:
        table_name=table_name.lower()
        
        if drop_table:
            exec_sql("DROP TABLE IF EXISTS {}".format(table_name))
            conn.commit()
            
       
        with open(file_name) as f:
            col_list= pd.read_csv(file_name, nrows=0, sep=sep)
            col_list=','.join(col_list.columns.values.tolist())
            #print(col_list)
            
            col_list=col_list.strip() \
                             .replace("Unnamed: 25","_Unnamed") \
                             .replace(" ","_") \
                             .replace("-","_") \
                             .replace(";",",") 
                             
            ssql=col_list.replace(","," varchar,")    
            ssql="CREATE TABLE IF NOT EXISTS {}({} varchar)".format(table_name,ssql)
            #print(col_list)
            exec_sql(ssql)
            
            conn.commit()
    except Exception as e:
        print('Error: ',e)                 
    finally:
        cur.close()
        conn.close()   
        
    return col_list
    
def copy_data_from_csv(file_name,table_name,col_list, sep=","):
    """
    copy from csv file to databse table
    """ 
    cur, conn= dal.connect_database()
    
    try:
        file_name=open(file_name, 'r')
        table_name=table_name.lower()
        
        copy_sql ="""
                    copy {} ({})
                    from stdin with
                    csv
                    header
                    delimiter as '{}'
                """.format(table_name,col_list, sep)
        #print(copy_sql)
        cur.copy_expert(sql=copy_sql, file=file_name)

        #print("end {}".format(table_name))
        conn.commit()     

    except Exception as e:
        print('Error: ',e)       
    finally:
        cur.close()
        conn.close()           