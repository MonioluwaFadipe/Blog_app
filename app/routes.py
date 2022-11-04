from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import LoginForm, RegistrationForm
from app.models import User, Article
from flask_login import login_user


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
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Unsucessful attempt. Please check your email or password', 'danger')
    return render_template('login.html', title='Register', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been successfully created", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

