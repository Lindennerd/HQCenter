from django.db import models
from django.contrib.auth.models import User

class User(User):
    profile_image = models.CharField(verbose_name=u'Avatar', max_length=200, blank=True)
    facebook = models.CharField(verbose_name=u'Facebook', max_length=200, blank=True)
    twitter = models.CharField(verbose_name=u'Twitter', max_length=200, blank=True) 
