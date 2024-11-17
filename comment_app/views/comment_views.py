class CommentView:
    @staticmethod
    def render_comment(comment):
        return {
            "comment_id": comment.comment_id,
            "post_id": comment.post_id,
            "user_id": comment.user_id,
            "content": comment.content,
            "created_at": comment.created_at,
            "updated_at": comment.updated_at
        }

    @staticmethod
    def render_comments(comments):
        return [CommentView.render_comment(comment) for comment in comments]

    @staticmethod
    def render_success(message, comment_id=None):
        response = {"message": message}
        if comment_id:
            response["comment_id"] = comment_id
        return response
