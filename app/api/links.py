from flask import Response, jsonify, make_response, request
from flask_restful import Resource, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

#resources importing
from models.users import Users
from models.links import Links
from api.errors import forbidden

class LinksApi(Resource):
    """
    Flask-restful resource for returning db.links collection.

    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add TasksApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(LinksApi, '/links/')

    """
    @jwt_required()
    def get(self) -> Response:
        """
        GET api to get all the tasks
        :return:JSON object
        """
        response_status = 500
        try:
            response_object = Links.objects()
            response_status = 200

        except Exception as err_msg:
            response_object = {'message': str(err_msg)}

        return jsonify({'result': response_object, 'status': response_status})

    @jwt_required()
    def post(self) -> Response:
        """
        POST api to create a task
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Links(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

class LinkApi(Resource):
    """
    Flask-resftul resource for returning db.links collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(LinkApi, '/link/<link_id>')
    """

    @jwt_required()
    def get(self, link_id: str) -> Response:
        """
        get single task document in tasks collection
        :param task_id:
        :return: JSON object
        """

        output = Links.objects.get(id=link_id)
        return jsonify({'result': output})

    @jwt_required()
    def put(self, link_id: str) -> Response:
        """
        to update task document in task collection
        :param link_id:
        :return: JSON object
        """
        data = request.get_json()
        put_user = Links.objects(id=link_id.update(**data))
        return jsonify({'result': put_user})

    @jwt_required()
    def delete(self, user_id: str) -> Response:
        """

        :param user_id:
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Links.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()