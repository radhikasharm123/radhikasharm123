import sys
import os
sys.path.append(os.getcwd())

from flask import Flask
from flask_migrate import Migrate
from shared.utils.db_utils import db
from comment_app.routes.comment_routes import comment_bp  # Ensure you have this file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:radheybhai@localhost:3306/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(comment_bp)
@app.route('/')
def index():
    return 'comment App is running'


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use a different port for this app
