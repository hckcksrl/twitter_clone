from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField('User_name',blank=True, max_length=255)
    header_image = models.ImageField(null = True)
    profile_image = models.ImageField(null = True)
    bio = models.CharField(max_length=100 , null = True)
    location = models.CharField(max_length= 100 , null = True)
    website = models.CharField(max_length=100 , null = True)
    theme_color = ColorField(default='#ccffff')
    birthday = models.CharField(max_length=100 , null = True)
    followers = models.ManyToManyField('self' , blank = True)
    following = models.ManyToManyField('self', blank = True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def follower_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()

    @property
    def tweet_count(self):
        return self.creators.all().count()