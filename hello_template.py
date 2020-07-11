from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    return render_template('hello_template.html', name = 'Haislan Montanha', gender = 'Female')

@app.route("/people/<name>/<gender>", methods=['GET'])
def people(name, gender):
    return render_template('hello_template.html', name=name, gender=gender )

app.run(debug=True)
