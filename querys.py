from connection_to_db import get_db_connection, release_db_connection
import psycopg2

# first query
def get_mission_by_year(year):
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
        calc_attack = [cur.execute(f"""
                SELECT air_force, COUNT(target_city) from mission
                where mission_date >= '01-01-{year}' and mission_date < '01-01-{year+1}'    
                group by air_force;
        """)]
        # מציאת הערך המקסימלי של התקיפות על ערים
        the_max_attack = max(calc_attack)

        # כאן אני מוצא את הערך המקסימלי ומחזיר את שם חיל האוויר שהוכנס לפניו לרשימה
        for i in the_max_attack:
            if i == the_max_attack:
                return calc_attack[i-1]
    except Exception as e:
        return e
    finally:
        release_db_connection(source_conn)

# second query
def bomb_damage_assessment():
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
        calc_damage = [cur.execute("""
        select target_city, count(bomb_damage_assessment)
        where attacking_aircraft > 5
        """)]
        the_max_damage = max(calc_damage)
        for i in calc_damage:
            if i == the_max_damage:
                return i, calc_damage[i - 1]
    except Exception as e:
        return e
    finally:
        release_db_connection(source_conn)




