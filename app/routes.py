from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm, RegistrationForm
from app.models import User, Article

posts = [
    {
        'author': 'Fadipe Daniel',
        'title': 'First Blog Post',
        'content': 'First Blog content',
        'date_posted': 'April 21, 2018'
    },

    {
        'author': 'Oni Temidayo',
        'title': 'Second Blog Post',
        'content': 'Second Blog content',
        'date_posted': 'April 4, 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in", "success")
            return redirect(url_for('home'))
        else:
            flash('Unsucessful attempt. Please check your username or password', 'danger')
    return render_template('login.html', title='Register', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Congratulations {form.username.data}. Your account has been created successfully!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

