class Article:
    articles = []
    article_id = 1

    def __init__(self, title, content):
        self.id = Article.article_id
        self.title = title
        self.content = content

        Article.article_id += 1
        Article.articles.append(self)

    @staticmethod
    def get_all_articles():
        return Article.articles

    @staticmethod
    def get_article_by_id(article_id):
        for article in Article.articles:
            if article.id == article_id:
                return article
        return None

    def save(self):
        Article.articles.append(self)
