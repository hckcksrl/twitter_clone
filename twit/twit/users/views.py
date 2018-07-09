from rest_framework.views import APIView
from rest_framework.response import Response
from . import models , serializers
from rest_framework import status
from twit.tweets import models as tweet_models
from django.db.models import Q

class Follower(APIView):

    def exist(self , user , follow_user):

        try : 

            user = models.User.objects.get(username = user).followers.get(username = follow_user)

            return user

        except models.User.DoesNotExist :

            return None

    def post(self , request , user_id , format=None):

        user = request.user

        try :

            follow_user = models.User.objects.get(id = user_id)

            exist_follow = self.exist(user,follow_user.username)

            if exist_follow is None : 

                user.followers.add(follow_user)

                user.save()

                return Response(status = status.HTTP_200_OK)

            else :

                user.followers.remove(follow_user)        

                return Response(status = status.HTTP_404_NOT_FOUND)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

    
class Following(APIView):

    def exist(self , user , follow_user):

        try : 

            user = models.User.objects.get(username = user).following.get(username = follow_user)

            return user

        except models.User.DoesNotExist :

            return None

    def post(self , request , user_id , format=None):

        user = request.user

        try :

            follow_user = models.User.objects.get(id = user_id)

            exist_follow = self.exist(user,follow_user.username)

            if exist_follow is None : 

                user.following.add(follow_user)

                user.save()

                return Response(status = status.HTTP_200_OK)

            else :

                user.following.remove(follow_user)        

                return Response(status = status.HTTP_404_NOT_FOUND)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)
  

class SmallRecommandList(APIView):

    def get(self , request , format=None):

        recommandlist = models.User.objects.all().order_by('date_joined')[:3]

        serializer = serializers.FollowListSerializer(recommandlist, many=True)

        return Response(data = serializer.data , status = status.HTTP_200_OK)


class FollowList(APIView):

    def get(self , request ,user_id, format=None):

        all_follower = models.User.objects.get(id = user_id).followers.all().order_by('username')

        serializer = serializers.FollowListSerializer(all_follower, many=True)

        return Response(data = serializer.data , status = status.HTTP_200_OK)


class FollowingList(APIView):
    
    def get(self , request ,user_id, format=None):

        all_following = models.User.objects.get(id = user_id).following.all().order_by('username')

        serializer = serializers.FollowListSerializer(all_following, many=True)

        return Response(data = serializer.data , status = status.HTTP_200_OK)

class SmallProfile(APIView):

    def get(self , request , user_id , format=None):

        try :

            user = models.User.objects.get(id = user_id)

            serializer = serializers.SmallProfileSerializer(user)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

class Search(APIView):

    def get(self , request , format=None):

        user = request.query_params.get('username',None)

        user_list = []

        try :

            search_username = models.User.objects.filter(Q(username__contains = user) | Q(name__contains = user)).distinct()[:3] 

            for username in search_username :

                user_list.append(username)

            serializer = serializers.SearchProfileSerializer(user_list , many = True)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        except models.User.DoesNotExist : 

            return Response(status = status.HTTP_404_NOT_FOUND)        
