from django.db import models
import uuid
from django.contrib.postgres.fields import JSONField


class Term(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    block = JSONField()

    class Meta:
        abstract = True


class Term1(Term):
    pass


class Term2(Term):
    pass


class Term3(Term):
    pass


class Term4(Term):
    pass
