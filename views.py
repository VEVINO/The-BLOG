from flask import render_template
from models import Article, Comment


def index():
    articles = Article.get_all_articles()
    return render_template('index.html', articles=articles)


def view_article(article_id):
    article = Article.get_article_by_id(article_id)
    comments = Comment.get_comments_for_article(article_id)
    return render_template('article.html', article=article, comments=comments)
