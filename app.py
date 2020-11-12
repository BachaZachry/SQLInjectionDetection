import flask
from flask import request,jsonify



def create_app():
    app = flask.Flask(__name__)
    @app.route('/v1/sanitized/input/',methods=['POST'])
    def check_input():
        #These are based on MySQL
        sql_injection_characters = ["'","--",";"]
        check_boolean = any(map(request.form['payload'].__contains__,sql_injection_characters))
        if check_boolean:
            return jsonify({"result":"unsanitized"})
        return jsonify({"result":"sanitized"})
    return app