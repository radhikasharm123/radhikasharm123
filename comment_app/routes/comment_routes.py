from flask import Blueprint
from comment_app.controllers.comment_controller import CommentController

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    return CommentController.create_comment(post_id)

@comment_bp.route('/api/posts/<int:post_id>/comments', methods=['GET'])
def get_comments_by_post(post_id):
    return CommentController.get_comments_by_post(post_id)
