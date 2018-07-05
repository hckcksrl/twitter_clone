from django.db import models
from twit.users import models as user_models

# Create your models here.
class TimeStampModel(models.Model):

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True

class Tweet(TimeStampModel):

    file = models.ImageField(null=True,blank=True)
    ids = models.ForeignKey('self', related_name = 'twits',on_delete=models.CASCADE , null=True , blank = True)
    content = models.TextField(null=True , blank=True)
    creator = models.ForeignKey(user_models.User, related_name='creators', on_delete=models.CASCADE)
    links = models.URLField(null=True)

    def __str__(self):
        return '{}'.format(self.content)


    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def tweet_count(self):
        return self.twits.all().count()

    @property
    def retweet_count(self):
        return self.retweet.all().count()


class Like(TimeStampModel):

    creator = models.ForeignKey(user_models.User , on_delete=models.CASCADE,null = True)
    tweet = models.ForeignKey(Tweet ,related_name = 'likes' , on_delete=models.CASCADE ,null = True)

    def __str__(self):

        return 'User : {} - Tweet ㅣ {}'.format(self.creator.username , self.tweet.content)


class Retweet(TimeStampModel):

    creator = models.ForeignKey(user_models.User , on_delete=models.CASCADE,null = True)
    retweet = models.ForeignKey(Tweet ,related_name = 'retweet' , on_delete=models.CASCADE ,null = True)

    def __str__(self):

        return 'User : {} - Tweet ㅣ {}'.format(self.creator.username , self.tweet.content)

