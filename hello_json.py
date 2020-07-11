from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/hello_json")
def form():
    return render_template('json_form.html')

@app.route("/json-return", methods=['POST'])
def handle_json():
    return jsonify(request.form)

app.run(debug=True)
