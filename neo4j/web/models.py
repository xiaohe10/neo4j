from django.db import models

# Create your models here.
from neo4django.db import models

class Person(models.NodeModel):
    weibo_ID = models.StringProperty()
    name = models.StringProperty()

    friends = models.Relationship('self',rel_type='follow')

