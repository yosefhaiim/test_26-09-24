from connection_to_db import get_db_connection, release_db_connection
import psycopg2

def normalize_db():
    source_conn = get_db_connection()
    target_conn = psycopg2.connect(
        dbname="test1db",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    try:
        cur = target_conn.cursor()
        s_cur = source_conn.cursor()
        s_cur.execute("SELECT * FROM customers")
        while True:
            customer_row = s_cur.fetchone()
            if customer_row is None:
                break

            mission_date = customer_row[1]
            target_ids = customer_row[13] # לא נכנס בהתחלה
            target_priority = customer_row[18]
            target_type = customer_row[16]

            cur.execute("INSERT INTO normal_missions (mission_date)"
            " VALUES (%s)",
            (mission_date))
            mission_id = cur.fetchone()[0]

            for target_id in target_ids:
                cur.execute("INSERT INTO normal_targets (customer_id, phone_number)"
                            " VALUES (%s, %s)",
                            (mission_id, target_id))

            cur.execute("INSERT INTO normal_targets (target_priority, target_type)"
            " VALUES (%s)",
            (target_priority, target_type))

    except Exception as e:
        print(e)
    finally:
        release_db_connection(source_conn)






