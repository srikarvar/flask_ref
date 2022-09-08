import mongoengine

from app import default_config

from types import FunctionType

def mongo(function: FunctionType) -> FunctionType:
    """
    Decorator method for running mongoengine before function execution.
    :param function:
    :return:
    """

    def load():
        mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        function()
    return load