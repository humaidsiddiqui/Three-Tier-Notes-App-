from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("running main")
    app.run(host="127.0.0.1", port=5000) 

























