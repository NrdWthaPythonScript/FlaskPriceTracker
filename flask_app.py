from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '42de87382667e241a46d0668e6744aaa'

@app.route("/home")
@app.route("/")
def home():
    form = LoginForm()
    return render_template('home.html', form=RegistrationForm)

@app.route("/about")
def about():
    return "<h1>About Page<h1>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register2.html', form=form)

@app.route("/login/")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
