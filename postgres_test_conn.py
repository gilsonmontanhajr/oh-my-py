from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


class pgUtil:
    def connect(pg_user, pg_pass, pg_host, pg_dbname):
        try:
            conn = psycopg2.connect(
                user=pg_user,
                password=pg_pass,
                host=pg_host,
                port="5432",
                database=pg_dbname)
            cursor = conn.cursor()
            print(conn.get_dsn_parameters(), "\n")
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as err:
            print("Error trying to connect ", err)

        return conn


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

    pg = pgUtil.connect(db_user, db_pass, db_uri, db_name)

    return render_template('pg_test.html', connect=pg)

app.run(debug=True)
