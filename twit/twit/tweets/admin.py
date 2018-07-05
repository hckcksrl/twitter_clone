from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'creator',
        'create_at',
        'update_at',
    )
    list_display_links = (
        'file',
        'creator',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'tweet',
        'creator',
        'create_at',
        'update_at',        
    )

@admin.register(models.Retweet)
class ReTweetAdmin(admin.ModelAdmin):

    list_display = (
        'retweet',
        'creator',
        'create_at',
        'update_at',        
    )
