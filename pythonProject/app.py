from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"


@app.route('/5')
def put5():
    return "поставте 5 пожалуйста"

if __name__ == "__main__":
    app.run(debug=True)
