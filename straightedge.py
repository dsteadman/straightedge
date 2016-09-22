import newspaper
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    cnn_paper = newspaper.build('http://cnn.com', memoize_articles=False)
    articles = cnn_paper.articles
    return render_template('homepage.html', articles=articles)
