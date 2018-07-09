from rest_framework import serializers
from . import models
from twit.tweets import models as tweet_models
from twit.tweets import serializers as tweet_serializers


class TwitSerializer(serializers.ModelSerializer):

    class Meta :
        model = tweet_models.Tweet
        fields = (
            'id',
            'twits',
            'create_at',
            'update_at',
            'file',
            'content',
            'creator',
            'tweet_count',
            'like_count',
            'retweet_count'
        )


class FollowListSerializer(serializers.ModelSerializer):

    class Meta :
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
        )

class SmallProfileSerializer(serializers.ModelSerializer):

    class Meta :
        model = models.User
        fields = (
            'header_image',
            'profile_image',
            'username',
            'name',
            'bio',
            'follower_count',
            'following_count',
            'tweet_count',
        )


class SearchProfileSerializer(serializers.ModelSerializer):

    class Meta : 
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name'
        )