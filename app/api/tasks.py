from flask import Response, jsonify, make_response, request
from flask_restful import Resource, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

#resources importing
from models.users import Users
from models.links import Links
from api.errors import forbidden

#mongoengine models importing
from models.tasks import Tasks

class TasksApi(Resource):
    """
    Flask-resftul resource for returning db.tasks collection.

    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add TasksApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(TasksApi, '/tasks/')

    """
    @jwt_required()
    def get(self) -> Response:
        """
        GET api to get all the tasks
        :return:JSON object
        """
        response_status = 500
        try:
            response_object = Tasks.objects()
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
            post_user = Tasks(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()


class TaskApi(Resource):
    """
    Flask-resftul resource for returning db.tasks collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(TaskApi, '/meal/<task_id>')
    """

    @jwt_required()
    def get(self, task_id: str) -> Response:
        """
        get single task document in tasks collection
        :param task_id:
        :return: JSON object
        """

        output = Tasks.objects.get(id=task_id)
        return jsonify({'result': output})

    @jwt_required()
    def put(self, task_id: str) -> Response:
        """
        to update task document in task collection
        :param task_id:
        :return: JSON object
        """
        data = request.get_json()
        put_user = Tasks.objects(id=task_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required()
    def delete(self, user_id: str) -> Response:
        """

        :param user_id:
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Tasks.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()


