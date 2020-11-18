import flask
from flask import request,jsonify



app = flask.Flask(__name__)

@app.route('/v1/sanitized/input/',methods=['POST'])
def check_input():
     #These are based on MySQL
     #Characters here have a potential use for SQL injection
     sql_injection_characters = ["'","--",";","`","/*","*/","#","OR 1=1"]
     check_boolean = any(map(request.form['payload'].__contains__,sql_injection_characters))
     if check_boolean:
          return jsonify({"result":"unsanitized"})
     return jsonify({"result":"sanitized"})

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=5001,debug = True)