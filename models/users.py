from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    StringField,
    EmailField,
    BooleanField,
    ReferenceField,
)

# flask packages
from flask_bcrypt import generate_password_hash, check_password_hash

# project resources
from models.products import Products

# external packages
import re


class Access(EmbeddedDocument):
    """
    Custom EmbeddedDocument to set user authorizations.
    :param user: boolean value to signify if user is a user
    :param admin: boolean value to signify if user is an admin
    """
    user = BooleanField(default=True)
    admin = BooleanField(default=False)


class Users(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param email: unique required email-string value
    :param password: required string value, longer than 6 characters
    :param access: Access object
    :param products: List of Product objects
    :param name: option unique string username
    :param phone: optional string phone-number, must be valid via regex
    """

    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))
    products = ListField(ReferenceField(Products))
    first_name = StringField(unique=False)
    last_name = StringField(unique=False)

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode("utf-8")

    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)

    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)
