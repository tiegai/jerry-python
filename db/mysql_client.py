import pymysql
from config import MYSQL_CONFIG

def get_mysql_data():
    conn = pymysql.connect(**MYSQL_CONFIG)
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM xxl_job_info LIMIT 10")  # 替换为你的表名
        result = cursor.fetchall()
    conn.close()
    return result
