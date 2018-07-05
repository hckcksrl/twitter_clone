from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path(
        "<str:username>",
        view = views.Tweets.as_view(),
        name = 'user_tweet'
    ),
    path(
        "<int:tweet_id>/tweet",
        view = views.CommentTweet.as_view(),
        name = 'comment_tweet'
    ),
    path(
        "",
        view = views.UploadTweet.as_view(),
        name = 'upload_tweet'
    ),
    path(
        "<int:tweet_id>/like",
        view = views.LikeTweet.as_view(),
        name = 'like_tweet'
    ),
    path(
        "<int:tweet_id>/retweet",
        view = views.ReTweet.as_view(),
        name = 'retweet'
    )
]
