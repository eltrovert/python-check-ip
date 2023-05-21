from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
@app.route('/', methods=["GET"])
def hello_world():
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    return jsonify({'version': "10000000000004", 'ip': request.environ['HTTP_X_FORWARDED_FOR'],'methods':'GET', 'ip3':str(request.headers)}), 200


if __name__ == "__main__":
    app.run(debug=True)
