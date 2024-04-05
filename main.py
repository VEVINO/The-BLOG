from flask import Flask, render_template, request, redirect, url_for, flash
from article import Article
from articles_data import ArticleData
from comment import Comment
from comments_data import CommentData

app = Flask(__name__)
app.secret_key = 'secret_key'

article_data = ArticleData()
comment_data = CommentData()


@app.route('/')
def index():
    articles = article_data.articles
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def view_article(article_id):
    article = next((article for article in article_data.articles if article['id'] == article_id), None)
    if article:
        comments = [comment['content'] for comment in comment_data.comments if comment['article_id'] == article_id]
        additional_info = "Aici puteți adăuga text suplimentar pentru articolul curent."
        if request.method == 'POST':
            content = request.form['content']
            if content not in [comment['content'] for comment in comment_data.comments]:
                new_comment = {"article_id": article_id, "content": content}
                comment_data.comments.append(new_comment)
            else:
                flash('Comentariul există deja!', 'error')
            return redirect(url_for('view_article', article_id=article_id))
        return render_template('article.html', article=article, comments=comments, additional_info=additional_info)
    else:
        return "Articolul nu există!"


@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title, content)
        new_article.save()
        return redirect(url_for('index'))
    return render_template('add_article.html')


@app.route('/article/<int:article_id>/add_comment', methods=['POST'])
def add_comment(article_id):
    content = request.form['content']
    existing_comments = Comment.get_comments_for_article(article_id)

    # Verificăm dacă comentariul există deja în lista de comentarii pentru articolul respectiv
    if content not in [comment.content for comment in existing_comments]:
        new_comment = Comment(article_id, content)
        new_comment.save()
    else:
        # Dacă comentariul este duplicat, afișăm un mesaj de eroare utilizatorului
        flash('Comentariul există deja!', 'error')

    return redirect(url_for('view_article', article_id=article_id))


if __name__ == '__main__':
    app.run(debug=True)
