from django.urls import path
from . import views 

urlpatterns =[
    path("",views.index,name="home"), #run function when app is accessed, this is the index /hello page
    path("learn/",views.learn,name="learn"),
    path("contributor/",views.contribute_index,name="contribute_index"),
    path("contributor/<str:contributor>/",views.contribute,name="contribute"),
    path("social_media/",views.social_media,name="social_media"),
    path("stories/",views.stories,name="stories"),
    path("events/",views.events,name="events"),
]