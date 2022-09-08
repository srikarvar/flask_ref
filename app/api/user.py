# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.users import Users
from api.errors import forbidden

class UsersApi(Resource):
    """
    Flask restful resource for getting db.user collection.

    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add UsersApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(UsersApi, '/user/')

    """

    @jwt_required
    def get(self) -> Response:
        """
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects()
            return jsonify({'result': output})
        else:
            return forbidden()


    @jwt_required
    def delete(self) -> Response:
        """
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects.delete()
            return jsonify({'result': output})
        else:
            return forbidden()

class UserApi(Resource):
    """
        Flask-resftul resource for returning db.user collection.
        :Example:
        >>> from flask import Flask
        >>> from flask_restful import Api
        >>> from app import default_config
        # Create flask app, config, and resftul api, then add UserApi route
        >>> app = Flask(__name__)
        >>> app.config.update(default_config)
        >>> api = Api(app=app)
        >>> api.add_resource(UserApi, '/user/<user_id>')
        """

    @jwt_required
    def get(self, user_id: str) -> Response:
        """
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects.get(id=user_id)
            return jsonify({'result': output})
        else:
            return forbidden()


    def put(self, user_id: str) -> Response:
        """

        :param user_id:
        :return: JSON object
        """
        """
                :return: JSON object
                """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Users.objects(id=user_id).update(**data)
            output = {'id': str(put_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    def post(self) -> Response:
        """

        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Users(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

    def delete(self, user_id: str) -> Response:
        """

        :param user_id:
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Users.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()