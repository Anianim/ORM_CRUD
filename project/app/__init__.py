from config import db
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_smorest import Api
from services.users import user_blp

import app.models

migrate = Migrate()


def create_app():
    application = Flask(__name__)
    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    application.config["API_TITLE"] = "My API"
    application.config["API_VERSION"] = "v1"
    application.config["OPENAPI_VERSION"] = "3.1.3"
    application.config["OPENAPI_URL_PREFIX"] = "/" # base url 
    application.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # 실제로 open api로 만들어진 결과물 
    application.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" # cdn adress
    
    db.init_app(application)
    migrate.init_app(application, db)
    
    api = Api(application)
    api.register_blueprint(user_blp)
    api.register_blueprint(question_blp)
    api.register_blueprint(submit_blp)
    api.register_blueprint(image_blp)
    api.register_blueprint(choice_blp)
    api.register_blueprint(questions_blp)

    # 블루 프린트 등록
    application.register_blueprint(user_blp, url_prefix='/user')

    return application