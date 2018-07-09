from django.urls import path
from twit.users import views


app_name = "users"
urlpatterns = [
    path(
        "<int:user_id>/follower",
        view = views.Follower.as_view(),
        name = 'user_follow'
    ),
    path(
        "<int:user_id>/following",
        view = views.Following.as_view(),
        name = 'user_following'
    ),
    path(
        'recommand',
        view = views.RecommandList.as_view(),
        name = 'all_follow_recommand'      
    ),
    path(
        "<int:user_id>/followlist",
        view = views.FollowList.as_view(),
        name = 'user_follow_list'
    ),
    path(
        "<int:user_id>/followinglist",
        view = views.FollowingList.as_view(),
        name = 'user_following_list'
    ),
    path(
        "<int:user_id>/smallprofile",
        view = views.SmallProfile.as_view(),
        name = 'small_profile'
    ),
    path(
        'search/',
        view = views.Search.as_view(),
        name = 'search'
    ),

]
