# Install the required package (if not installed)
# pip install mysql-connector-python
import pymysql
pymysql.install_as_MySQLdb()
import mysql.connector

try:
    # Connect to MySQL server (without specifying a database)
    dataBase = mysql.connector.connect(
        host="localhost",
        user="mohamed",          # MySQL username
        password="Moha2426###" ,  # MySQL password
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object
    cursorObject = dataBase.cursor()

    # Create a new database (IF NOT EXISTS avoids errors if DB already exists)
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS mohamed")
    print("✅ Database 'mohamed' created successfully!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    # Close cursor and connection
    if 'cursorObject' in locals():
        cursorObject.close()
    if 'dataBase' in locals() and dataBase.is_connected():
        dataBase.close()