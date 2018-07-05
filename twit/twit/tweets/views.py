from rest_framework.views import APIView
from rest_framework.response import Response
from . import models , serializers
from rest_framework import status
from twit.users import models as user_models

#   list(serializer.data[0].values())[1]  시리얼라이저 안의 밸류값 구하는법
#   list(request.data.values())[0] request 의 밸류값 구하는법
#   print(self.request.path)    request path 구하는법

class Tweets(APIView):

    def get(self , request , username , format=None):

        user = request.user

        try :

            users = user_models.User.objects.get(username=username)

            tweet = models.Tweet.objects.filter(creator_id = users.id)

            if tweet is not None :

                    serializer = serializers.TweetSerializer(tweet , many=True)

                    return Response(data = serializer.data , status = status.HTTP_200_OK)

            else :

                return Response(status = status.HTTP_204_NO_CONTENT)

        except user_models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

class CommentTweet(APIView):

    def post(self , request ,tweet_id, format=None):

        user = request.user
        
        try :
            
            tweet = models.Tweet.objects.get(id = tweet_id)

            serializer = serializers.TweetSerializer(data = request.data,partial=True)

            if serializer.is_valid():

                serializer.save(creator = user , ids = tweet )

                return Response(data =serializer.data , status = status.HTTP_200_OK)

            else :

                return Response(data = serializer.errors , status = status.HTTP_404_NOT_FOUND)

        except models.Tweet.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)


    def get(self , request , tweet_id , format = None):

        user = request.user

        try :

            tweet = models.Tweet.objects.filter(id = tweet_id)

            if tweet is not None :

                serializer = serializers.TweetSerializer(tweet , many=True)
            
                return Response(data = serializer.data , status = status.HTTP_200_OK)

            else :

                return Response(data = serializer.errors , status = status.HTTP_204_NO_CONTENT)

        except user_models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

class UploadTweet(APIView):

    def post(self , request , format=None):

        user = request.user

        serializer = serializers.UploadTweetSerializer(data = request.data,partial=True)

        if serializer.is_valid():

            serializer.save(creator = user)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        else :

            return Response(data = serializer.errors , status = status.HTTP_404_NOT_FOUND)

class LikeTweet(APIView):

    def exist(self , tweet_id, user_id):

        try : 
            
            like = models.Like.objects.get(tweet_id = tweet_id , creator_id = user_id)

            return like

        except models.Like.DoesNotExist :

            return None


    def post(self , request , tweet_id , format=None):

        user = request.user

        try :

            tweet = models.Tweet.objects.get(id = tweet_id)

            like = self.exist(tweet_id , user.id)

            if like is None :

                likes = models.Like.objects.create(creator = user, tweet = tweet )

                likes.save()

                return Response(status = status.HTTP_200_OK)

            else :

                like.delete()
  
                return Response(status = status.HTTP_204_NO_CONTENT)

        except models.Tweet.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

#   링크주소 있으면 

class ReTweet(APIView):

    def exist(self , retweet_id, user_id):

        try : 
            
            retweet = models.Retweet.objects.get(retweet_id = retweet_id , creator_id = user_id)

            return retweet

        except models.Retweet.DoesNotExist :

            return None


    def post(self , request , tweet_id , format=None):

        user = request.user

        try :

            tweet = models.Tweet.objects.get(id= tweet_id)

            retweet = self.exist(tweet_id , user.id)

            if retweet is None :

                retweets = models.Retweet.objects.create(creator = user , retweet = tweet)
                
                serializer = serializers.TweetSerializer(data = request.data , partial=True)

                if serializer.is_valid():

                    serializer.save(creator = user,links= 'localhost:8000/tweets/{tweet_id}/tweet')

                    retweets.save()

                    return Response(data = serializer.data , status = status.HTTP_200_OK)

                else :

                    return Response(data = serializer.errors , status = status.HTTP_404_NOT_FOUND)

            else:

                retweet.delete()

                return Response(status = status.HTTP_404_NOT_FOUND)

        except models.Tweet.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)



