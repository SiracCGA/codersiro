# import flast module
from flask import Flask

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/dnm")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':  
   app.run(host='codersiro.xyz')  
