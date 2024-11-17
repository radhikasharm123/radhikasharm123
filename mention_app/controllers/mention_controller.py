"""from flask import request, jsonify
from mention_app.services.mention_service import MentionService
from shared.models.mention_model import Mention
from shared.utils.db_utils import db  # Import the db object

class MentionController:
    @staticmethod
    def get_all_mentions():
        mentions = Mention.query.all()
        mention_list = [
            {
                "mention_id": mention.mention_id,
                "mentioned_user_id": mention.mentioned_user_id,
                "comment_id": mention.comment_id,
                "created_at": mention.created_at
            }
            for mention in mentions
        ]
        return jsonify(mention_list), 200

    @staticmethod
    def create_mention():
        data = request.get_json()
        if not data.get("mentioned_user_id") or not data.get("comment_id"):
            return jsonify({"error": "Missing required fields"}), 400

        try:
            mention = MentionService.create_mention(
                mentioned_user_id=data["mentioned_user_id"],
                comment_id=data["comment_id"]
            )
            return jsonify({
                "mention_id": mention.mention_id,
                "mentioned_user_id": mention.mentioned_user_id,
                "comment_id": mention.comment_id,
                "created_at": mention.created_at
            }), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_mention(mention_id):
        mention = Mention.query.get(mention_id)
        if not mention:
            return jsonify({"error": "Mention not found"}), 404
        return jsonify({
            "mention_id": mention.mention_id,
            "mentioned_user_id": mention.mentioned_user_id,
            "comment_id": mention.comment_id,
            "created_at": mention.created_at
        }), 200

    @staticmethod
    def delete_mention(mention_id):
        mention = Mention.query.get(mention_id)
        if not mention:
            return jsonify({"error": "Mention not found"}), 404
        try:
            db.session.delete(mention)  # db is now correctly imported
            db.session.commit()
            return jsonify({"message": "Mention deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500"""
            


from flask import request, jsonify
from mention_app.services.mention_service import MentionService
from shared.models.mention_model import Mention
from shared.utils.db_utils import db  # Import the db object

class MentionController:
    @staticmethod
    def get_all_mentions():
        mentions = Mention.query.all()
        mention_list = [
            {
                "mention_id": mention.mention_id,
                "mentioned_user_id": mention.mentioned_user_id,
                "comment_id": mention.comment_id,
                "post_id": mention.post_id,
                "created_at": mention.created_at
            }
            for mention in mentions
        ]
        return jsonify(mention_list), 200

    @staticmethod
    def create_mention():
        data = request.get_json()
        if not data.get("mentioned_user_id") or not (data.get("comment_id") or data.get("post_id")):
            return jsonify({"error": "Missing required fields"}), 400

       # if not data.get("comment_id") and not data.get("post_id"):
           # return jsonify({"error": "You must specify either a comment_id or a post_id"}), 400

        try:
            mention = MentionService.create_mention(
                mentioned_user_id=data["mentioned_user_id"],
                comment_id=data.get("comment_id"),
                post_id=data.get("post_id")
            )
            return jsonify({
                "mention_id": mention.mention_id,
                "mentioned_user_id": mention.mentioned_user_id,
                "comment_id": mention.comment_id,
                "post_id": mention.post_id,
                "created_at": mention.created_at
            }), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_mention(mention_id):
        mention = Mention.query.get(mention_id)
        if not mention:
            return jsonify({"error": "Mention not found"}), 404
        return jsonify({
            "mention_id": mention.mention_id,
            "mentioned_user_id": mention.mentioned_user_id,
            "comment_id": mention.comment_id,
            "post_id": mention.post_id,
            "created_at": mention.created_at
        }), 200

    @staticmethod
    def delete_mention(mention_id):
        mention = Mention.query.get(mention_id)
        if not mention:
            return jsonify({"error": "Mention not found"}), 404
        try:
            db.session.delete(mention)
            db.session.commit()
            return jsonify({"message": "Mention deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
