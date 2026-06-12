# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="student_db"
# )

# print("Connected Successfully")


import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )
print("Connected Successfully")
