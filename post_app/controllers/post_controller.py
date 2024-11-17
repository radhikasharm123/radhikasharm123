from flask import request
from flask import jsonify
from post_app.services.post_service import PostService
from post_app.views.post_views import PostView

class PostController:
    @staticmethod
    def get_all_posts():
        posts = PostService.get_all_posts()
        return PostView.render_posts(posts), 200

    @staticmethod
    def get_post(post_id):
        post = PostService.get_post(post_id)
        return post

    @staticmethod
    def create_post():
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')

        post = PostService.create_post(user_id, content)
        return PostView.render_success('Post created successfully', post.post_id), 201

    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        new_content = data.get('new_content')
        if not new_content:
            return jsonify({"error": "Content is required"}), 400
        
        updated_post = PostService.update_post(post_id, new_content)
        if updated_post:
            # Return a JSON response indicating success
            return jsonify({
                "message": "Post updated successfully",
                "post": {
                    "post_id": updated_post.post_id,
                    "content": updated_post.content
                }
            }), 200
        else:
            # Return an error if the post was not found
            return jsonify({"error": "Post not found"}), 404
            return post

    @staticmethod
    def delete_post(post_id):
        post = PostService.delete_post(post_id)
        if post:
            # Return a JSON response indicating success
            return jsonify({"message": "Post deleted successfully"}), 200
        else:
            # Return a JSON response indicating post was not found
            return jsonify({"error": "Post not found"}), 404
        return post