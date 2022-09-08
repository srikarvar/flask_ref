from flask_restful import Api

#apis import
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.tasks import TasksApi, TaskApi
from api.links import LinksApi, LinkApi


def create_routes(api):
    api.add_resource(TasksApi, '/tasks/')
    api.add_resource(TaskApi, '/tasks/<task_id>')

    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(LinksApi, '/links/')
    api.add_resource(LinkApi, '/links/<link_id>')

