from datetime import timedelta

from flask import Flask, jsonify
from flask_restful import Api
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.resources.user_resource import user_api
from app.resources.comic_resource import comic_api
from flask_cors import CORS
from .ext import ma, migrate
from flask_jwt_extended import JWTManager


def create_app(settings_module):
    app = Flask(__name__)
    config(app)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    Api(app, catch_all_404s=True)
    app.url_map.strict_slashes = False
    app.register_blueprint(user_api)
    app.register_blueprint(comic_api)

    CORS(app)
    register_error_handlers(app)

    jwt = JWTManager(app)

    return app


def config(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://hisrcbfjjahwnz:70e1556eec9e757854a1626ee3fdfbced1d162c68af2bda1410040f6745b43ef@ec2-54-160-103-135.compute-1.amazonaws.com/des0bsn8389if4'
    app.config["JWT_SECRET_KEY"] = "XKCD-secret"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
