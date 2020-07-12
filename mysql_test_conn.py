from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MYSQL TREATMENT

class mysql_util():
    def connect(uri, user, passwd):

        try:
            conn = mysql.connector.connect(
                host=uri,
                user=user,
                password=passwd
            )
            print(conn.get_server_info())

        except mysql.connector.Error as err:
            print("Error trying to connect : ", err)

        return conn

@app.route("/my", methods=['GET'])
def mysql_connect_form():
    return render_template("my_connect.html")


@app.route("/my_test", methods=['POST'])
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

    return render_template('my_test.html', connect=my.connect(db_uri, db_user, db_pass))

app.run(debug=True)

