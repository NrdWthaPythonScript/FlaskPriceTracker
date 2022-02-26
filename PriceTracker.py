from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/home")
def hoe():
    return "<h1>Hooooome Page<h1>"

if __name__ == '__main__':
    app.run(debug=True)
