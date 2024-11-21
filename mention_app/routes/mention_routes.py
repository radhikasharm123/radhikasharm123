
    
from flask import Blueprint
from mention_app.controllers.mention_controller import MentionController

mention_bp = Blueprint('mention_bp', __name__)

@mention_bp.route('/api/mentions', methods=['GET'])
def get_all_mentions():
    return MentionController.get_all_mentions()

@mention_bp.route('/api/mentions', methods=['POST'])
def create_mention():
    return MentionController.create_mention()

@mention_bp.route('/api/mentions/<int:mention_id>', methods=['GET'])
def get_mention(mention_id):
    return MentionController.get_mention(mention_id)

@mention_bp.route('/api/mentions/<int:mention_id>', methods=['DELETE'])
def delete_mention(mention_id):
    return MentionController.delete_mention(mention_id)
