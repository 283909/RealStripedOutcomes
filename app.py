# flask is framework in python

from flask import Flask

app = Flask(__name__)
# route is url  it is a path of url @ is decorated in python 

@app.route("/")
def hello_world():
    return "Hello, World!"

export FLASK_APP=app.py
Flask $ python app.py

print(__name__)
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
    
    