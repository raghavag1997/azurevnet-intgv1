from flask import Flask,render_template, request
import pyodbc

server = 'tcp:poc321.database.windows.net'
database = 'mydb'
username = 'admin321'
password = 'Ragh@db31'
driver = '{ODBC Driver 17 for SQL Server}'


cnxn = pyodbc.connect('DRIVER=' + driver +
                      ';SERVER=' + server +
                      ';DATABASE=' + database +
                      ';UID=' + username +
                      ';PWD=' + password)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/getdata")
def getdata():
    cursor = cnxn.cursor()
    print('Connection established')
    cursor.execute("select * from MyUsers;")
    data=cursor.fetchall()
    print(data)
    return str(data)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
