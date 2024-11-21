
import sys
import os
sys.path.append(os.getcwd())
    
from flask import Flask
from mention_app.routes.mention_routes import mention_bp
from shared.utils.db_utils import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:radheybhai@localhost:3306/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(mention_bp)

@app.route('/')
def index():
    return 'Mention App is running'

if __name__ == '__main__':
    app.run(debug=True, port=5002)
