from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from FlaskBlog.Config import Config

# 建立database物件
db = SQLAlchemy()

# 加密用
bcrypt = Bcrypt()

# 登入管理員
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)

    # 利用物件做設定
    app.config.from_object(Config)

    # 初始化
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from FlaskBlog.users.Routes import users
    from FlaskBlog.posts.Routes import posts
    from FlaskBlog.main.Routes import main
    from FlaskBlog.errors.Handlers import errors

    # 將blueprint註冊到app裡
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app