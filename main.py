from db.mysql_client import get_mysql_data
from api.springboot_client import call_springboot_api, call_springboot_api_no_body


def main():
    mysql_data = get_mysql_data()
    print("MySQL 数据:", mysql_data)

    response = call_springboot_api_no_body()
    print("Spring Boot API 响应:", response)

if __name__ == "__main__":
    main()
