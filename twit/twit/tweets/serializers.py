from rest_framework import serializers
from . import models
from twit.users import models as user_models
from twit.users import serializers as user_serializers

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data



class ReTweetUserSerializer(serializers.ModelSerializer):

    class Meta :
        model = user_models.User
        fields= (
            'id',
            'username',
            'name'
        )


class ReTweetContentSerializer(serializers.ModelSerializer):

    creator = ReTweetUserSerializer(read_only = True)

    class Meta :
        model = models.Tweet
        fields = (
            'id',
            'file',
            'content',
        )

class PostUserSerializer(serializers.ModelSerializer):

    class Meta :
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )

class RetweetSerializer(serializers.ModelSerializer):

    class Meta :
        model = models.Retweet
        fields = '__all__'

class TweetSerializer(serializers.ModelSerializer):

    creator = PostUserSerializer()
    # twits = user_serializers.TwitSerializer(many=True)
    twits = RecursiveField(many=True)
    class Meta :
        model = models.Tweet
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


class LikeSerializer(serializers.ModelSerializer):

    class Meta :
        model = models.Like
        fields = '__all__'


class UploadTweetSerializer(serializers.ModelSerializer):

    creator = PostUserSerializer()

    class Meta :
        model = models.Tweet
        fields = (
            'id',
            'file',
            'content',
            'creator',
        )
