from flask import request
from comment_app.services.comment_service import CommentService
from comment_app.views.comment_views import CommentView

class CommentController:
    @staticmethod
    def create_comment(post_id):
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')
        comment = CommentService.create_comment(post_id, user_id, content)
        return CommentView.render_success('Comment added', comment.comment_id), 201

    @staticmethod
    def get_comments_by_post(post_id):
        comments = CommentService.get_comments_by_post(post_id)
        return CommentView.render_comments(comments), 200
