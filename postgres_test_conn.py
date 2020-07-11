from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


class pg_util:
    def pg_connect(pg_user, pg_pass, pg_host, pg_dbname):
        try:
            connection = psycopg2.connect(
                host=pg_host,
                user=pg_user,
                password=pg_pass,
                dbname=pg_dbname
            )
        except:
            connection = None

        return connection


@app.route("/pg", methods=['GET'])
def pg_connect_form():
    return render_template("pg_connect.html")

@app.route("/pg_test", methods=['POST'])
def pg_test_conn():
    db_uri = request.form['db_uri']
    db_user = request.form['db_user']
    db_pass = request.form['db_pass']
    db_name = request.form['db_name']

    print("db_uri = " + db_uri)
    print("db_user = " + db_user)
    print("db_pass = " + db_pass)
    print("db_name = " + db_name)

    pg = pg_util
    conn_return = pg.pg_connect(
        db_uri,
        db_user,
        db_pass,
        db_name
    )
    return render_template('pg_test.html', connect=conn_return)

app.run(debug=True)
