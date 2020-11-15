
# mongo-engine packages
from mongoengine import Document, StringField, FloatField


class Products(Document):
    """
    Template for a mongoengine document, which represents products.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    :Example:
    >>> import mongoengine
    >>> from app import default_config
    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    >>> new_product = Products(name= "hot wheels  hyperfin", \
                        description= "From the Fast & Furious Spy Racers", \
                        price= "69000")
    >>> new_product.save()
    <Product: Product object>
    """

    name = StringField(required=True)
    description = StringField(max_length=240)
    price = FloatField()
    image_url = StringField()