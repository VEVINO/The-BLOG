class Comment:
    comments = []
    comment_id = 1

    def __init__(self, article_id, content):
        self.id = Comment.comment_id
        self.article_id = article_id
        self.content = content
        Comment.comment_id += 1
        Comment.comments.append(self)

    @staticmethod
    def get_comments_for_article(article_id):
        return [comment for comment in Comment.comments if comment.article_id == article_id]

    def save(self):
        Comment.comments.append(self)
