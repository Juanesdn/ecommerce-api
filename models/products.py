
# mongo-engine packages
from mongoengine import Document, StringField, FloatField


class Products(Document):
    """
    Template for a mongoengine document, which represents products.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    """

    name = StringField(required=True)
    category = StringField(required=True)
    description = StringField(max_length=240)
    price = FloatField()
    image_url = StringField()
