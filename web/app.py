from flask import Flask, request
from methods_account import idf_method_account
from methods_user import idf_method

app = Flask(__name__)



@app.route('/')


@app.route('/account', methods = ['POST'])
def account():
    data = request.json
    return (idf_method_account(data))


@app.route('/user', methods = ['POST'])
def user():
    data = request.json
   
    return (idf_method(data))


if __name__ == "__main__":
    app.run(debug=True, port=5002)
