"""from shared.models.mention_model import Mention
from shared.utils.db_utils import db

class MentionService:
    @staticmethod
    def create_mention(mentioned_user_id, comment_id):
        mention = Mention(mentioned_user_id=mentioned_user_id, comment_id=comment_id)
        db.session.add(mention)
        db.session.commit()
        return mention"""

from shared.models.mention_model import Mention
from shared.utils.db_utils import db

class MentionService:
    @staticmethod
    def create_mention(mentioned_user_id, comment_id=None, post_id=None):
        if not comment_id and not post_id:
            raise ValueError("Either comment_id or post_id must be provided.")

        mention = Mention(
            mentioned_user_id=mentioned_user_id,
            comment_id=comment_id,
            post_id=post_id
        )
        db.session.add(mention)
        db.session.commit()
        return mention
