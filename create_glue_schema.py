import boto3
import csv
import pyarrow as pa
import pyarrow.parquet as pq
import mysql.connector
import pandas as pd

def sql2df(connection, sql_statement):
    """Executes a SQL query against a MySQL database and returns a Pandas DataFrame.

    Args:
        connection (mysql.connector.MySQLConnection): An established MySQL connection.
        sql_statement (str): The SQL query to execute.

    Returns:
        pandas.DataFrame: A DataFrame containing the query results.
    """

    try:
        cursor = connection.cursor()
        cursor.execute(sql_statement)
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=column_names)
        return df
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None

# Example usage

glue_database_name = 'my_database'
s3_data_bucket = 'your-s3-bucket'

# Create Boto3 clients for Glue 
glue_client = boto3.client('glue')

# Helper function to map Parquet types to Glue types
def convert_parquet_type_to_glue(parquet_type):
    if isinstance(parquet_type, pa.types.is_string):
        return 'string'
    elif isinstance(parquet_type, pa.types.is_integer):
        return 'int'
    elif isinstance(parquet_type, pa.types.is_float):
        return 'double'
    elif isinstance(parquet_type, pa.types.is_boolean):
        return 'boolean'
    # ... add more mappings as needed
    else:
        return 'string'  # Default to string for unhandled types


if __name__ == '__main__':
    config = {
        "host": "54.162.42.172",
        "user": "stockairo",
        "password": "make-sql-from-text-4-all",
        "database": "svday_etfdb"
    }

    mydb = mysql.connector.connect(**config)
    sql_meta_query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'svday_etfdb'"
    meta_df = sql2df(mydb, sql_meta_query)
    mydb.close()


    tables = meta_df['table_name'].unique()

    for table in tables:

        tab_cols = meta_df[meta_df['table_name'] == table]

        # Read schema from Parquet file
        parquet_file = pq.ParquetFile(f's3://{s3_data_bucket}/path/to/data/{table_name}/data.parquet') # Example path
        parquet_schema = parquet_file.schema

        # Build Glue schema from Parquet schema
        for field in parquet_schema:
            schema.append({'Name': field.name, 'Type': convert_parquet_type_to_glue(field.type)})

        # Create the Glue table
        try:
            glue_client.create_table(
                DatabaseName=glue_database_name,
                TableInput={
                    'Name': table_name,
                    'TableType': 'EXTERNAL_TABLE',
                    'StorageDescriptor': {
                        'Columns': schema,
                        'Location': f's3://{s3_data_bucket}/path/to/data/{table_name}/' 
                    }
                }
            )
            print(f'Glue table {table_name} created successfully.')
        except glue_client.exceptions.AlreadyExistsException:
            print(f'Glue table {table_name} already exists.')
