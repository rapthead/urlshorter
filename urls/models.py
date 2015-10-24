from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator

class Url(models.Model):
    url = models.CharField(max_length=65535, validators=[URLValidator(['http', 'https'])], blank=False)
    created = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, blank=False, unique=True)
    user = models.ForeignKey(User, blank=False)
    def views(self):
        return self.view_set.values('session_id').distinct().count()

class View(models.Model):
    session_id = models.CharField(max_length=256, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    url = models.ForeignKey(Url, blank=False)
