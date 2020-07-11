from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MYSQL TREATMENT

class mysql_util():
    def connect(uri, user, passwd, dbname):
        mydb = mysql.connector.connect(
            host=uri,
            user=user,
            password=passwd
        )
        return mydb

@app.route("/mysql", methods=['GET'])
def mysql_connect_form():
    return render_template("mysql_connect.html")


@app.route("/mysql_connect", methods=['POST'])
def mysql_connect():
    # vars
    db_uri = request.form['db_uri']
    db_user = request.form['db_user']
    db_pass = request.form['db_pass']
    db_name = request.form['db_name']

    print("db_uri = " + db_uri)
    print("db_user = " + db_user)
    print("db_pass = " + db_pass)
    print("db_name = " + db_name)

    # Creating object
    my = mysql_util
    #my.connect(db_uri, db_user, db_pass, db_name)

    return render_template('mysql_test.html', connect=my.connect(db_uri, db_user, db_pass, db_name))

app.run(debug=True)

