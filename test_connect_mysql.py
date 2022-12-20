import mysql.connector
from mysql.connector import Error



connection = mysql.connector.connect(host='toraq-staging.cluster-chqhep6ovkvr.ap-southeast-1.rds.amazonaws.com',
                             database='toraq_staging',
                             user='silo',
                             password='AJMlQ3nw0zAawEPwvjjwAz')

if connection.is_connected():
 db_Info = connection.get_server_info()
 print("Connected to MySQL Server version ", db_Info)