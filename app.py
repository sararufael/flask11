from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
db = SQLAlchemy(application)

from routes import app
application.register_blueprint(app)


if __name__=='__main__':
    db.create_all()
    application.run()