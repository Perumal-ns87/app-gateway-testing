from flask import Flask # type: ignore
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, Here I can use private endpoint for accessing the application'

if __name__ == '__main__':
    app.run(debug=True)