from random import choice
from typing import Type
from flask_mongoengine import Document

def get_random(object_type: Type[Document], quantity=1) -> list:
    """
    Get random document list from MongoDB collection
    :param object_type:
    :param quantity:
    :return:
    """
    rand_list = []
    id_list = object_type.objects.only('id')
    for _ in range(quantity):
        dish_id = choice(id_list)['id']
        rand_list.append(object_type.objects(id=dish_id).next())
    return rand_list

