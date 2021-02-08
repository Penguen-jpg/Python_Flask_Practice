import os

class Config:
    # 加密用(防止一些網路攻擊)
    SECRET_KEY = "fd97c3b731df463ea2336d56f3fdddea"

    # 使用sqlite資料庫連線
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" 

    # 設定郵件伺服器
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')