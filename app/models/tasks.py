"""
__author__ == Sai Srikar Varanasi
"""

from mongoengine import Document, StringField, FloatField, BooleanField

class Tasks(Document):
    """
        Template for a mongoengine document, which represents a user's favorite meal.
        :param task: required string value
        :param done: Boolean value
        :param description: optional string value

        :Example:
        >>> import mongoengine
        >>> from app import default_config
        >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
        MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
        >>> new_task = Tasks(name= "Vegetable Spring Rolls", \
                            description= "These crisp veggie rolls are filled with"  \
                                         "cabbage, peppers, cucumber, and home-made peanut sauce.")
        >>> new_task.save()
        <Task: Task object>
        """

    task = StringField(required=True)
    done = BooleanField(required=True)
    description = StringField

