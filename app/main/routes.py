from flask import render_template, request, Blueprint
from app.models import Article

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    posts = Article.query.all()
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/contact")
def contact():
    return render_template('contact.html')

