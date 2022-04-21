import psycopg2
from psycopg2.extras import RealDictCursor, DictCursor

# Connect to database
conn = psycopg2.connect("dbname='CLASSIFIED' user='CLASSIFIED' host='CLASSIFIED' password='CLASSIFIED' port='CLASSIFIED'")

def get_rows(sql_query, cursor_factory=RealDictCursor):
    """
    The get_rows function takes the SQL Query and calls to the database and returns the values as a Python readable class
    :param sql_query: The SQL query to run
    :param cursor_factory: Defaulted at RealDictCursor to return the RealDict class that can only be iterated through by key
    :return: returns a Python readable representation of the table
    """
    cur = conn.cursor(cursor_factory=cursor_factory)
    cur.execute(sql_query)
    rows = cur.fetchall()
    cur.close()
    return rows


def create_table(table_name, cursor_factory=RealDictCursor):
    """
    Creates a table of the the name 'table_name' in the database that is connected
    :param table_name: The name of the table to be created
    :param cursor_factory: Defaulted at RealDictCursor to return the RealDict class that can only be iterated through by key
    """
    cur = conn.cursor(cursor_factory=cursor_factory)
    sql = '''CREATE TABLE frank.%s (
                        hubspot_id BIGINT PRIMARY KEY,
                        db_id BIGINT
            );''' % (table_name)
    cur.execute(sql, table_name)
    # commit the changes
    conn.commit()
    cur.close()
 
def add_to_db(ids, table_name, cursor_factory=RealDictCursor):
    """
    Adds the hubspot_id and database_id for the OBJECTS depending on the 'table_name' parameter
    :param ids: Tuple of (hubspot_id, db_id)
    :param table_name: The name of the table to add the values to
    :param cursor_factory: Defaulted at RealDictCursor to return the RealDict class that can only be iterated through by key
    """
    cur = conn.cursor(cursor_factory=cursor_factory)
    args_str = ','.join(cur.mogrify("(%s,%s)", x).decode("utf-8") for x in ids)
    sql = """INSERT INTO frank.%s (hubspot_id, db_id) VALUES """ % (table_name)
    cur.execute(sql + args_str)
    conn.commit()
    cur.close()

