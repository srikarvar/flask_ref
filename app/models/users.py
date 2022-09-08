from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         StringField,
                         EmailField,
                         BooleanField,
                         ReferenceField)

from flask_bcrypt import generate_password_hash, check_password_hash

#project resources
from models.tasks import Tasks
from models.links import Links

import re

class Access(EmbeddedDocument):
    """
    Custom EmbeddedDocument to set user authorizations.


    :param user: boolean value to signify if user is a user
    :paramadmin: boolean value to signify is user is admin

    """

    user = BooleanField(default=True)
    admin = BooleanField(default=False)

class Users(Document):
    """
    Template for a mongoengine document which represents a user
    Password is automatically hashed before saving.

    :param email: unique required email string value
    :param password: required string value, longer than 6 charcaters
    :param access: Access object
    :param tasks: List of Tasks
    :param name: option unique string username

    :Example:
    >>> import mongoengine
    >>> from app import default_config

    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    # Create test user
    >>> new_user = Users(email="test@test.com", password="hunter2", access={"admin": True})
    >>> new_user.save()
    >>> new_user.name = "testuser"
    >>> new_user.save()
    # Remove test user
    >>> new_user.delete()
    .. seealso:: :class:`Access`, :class:`Phone`, :class:`models.tasks.Tasks`
    """

    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))
    tasks = ListField(ReferenceField(Tasks))
    links = ListField(ReferenceField(Links))
    name = StringField(unique=False)

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    # Use documentation Bcrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)
    # Use documentation from BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate hash prior to saving
        if self._created:
            self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)



