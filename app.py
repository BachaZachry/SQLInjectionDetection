import flask
from flask import request,jsonify

app = flask.Flask(__name__)


@app.route('/v1/sanitized/input/',methods=['POST'])
def check_input():
    #These are based on MySQL
    sql_injection_characters = ["'","--",";"]
    check_boolean = any(map(request.form['payload'].__contains__,sql_injection_characters))
    if check_boolean:
        return jsonify({"result":"unsanitized"})
    return jsonify({"result":"sanitized"})

if __name__ == '__main__':
    app.debug = True
    app.run()