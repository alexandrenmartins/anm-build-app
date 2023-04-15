import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '<h1><p style="color:' + os.environ.get('APP_COLOR', 'black') + '">Trabalho Infnet - Prática 2: BuildApp</p></h1>'

@app.route('/api')
def hello():
    return '{status: ok}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
