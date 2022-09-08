from mongoengine import Document, StringField, FloatField, BooleanField

class Links(Document):
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
        >>> new_link = Links(name= "Notion", \
                            uri= "www.notion.com")
        >>> new_link.save()
        <Link: Link object>
        """

    name = StringField(required=True)
    uri = StringField(required=True)

