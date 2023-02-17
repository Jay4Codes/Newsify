from django.urls import path,include
from .views import RegistrationAPI,LoginAPI, UserAPI,createprofile,profileDetail
from . import views
from knox import views as knox_views
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)

router.register('profile-image', views.createnewsapi)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('userdetail',UserAPI.as_view(),name='userdetail'),
    path('profilecreate/',createprofile.as_view(),name='profilecreate'),
    path('profileDetail/',profileDetail.as_view(),name='profiledetail'),
    path('newsapi/',views.newsapi.as_view(),name='newsapi'),
    path('newssources/',views.newsSources.as_view(),name='newsSources'),
    path('profileposts/<int:pk>/',views.profileposts.as_view(),name='profileposts'),


   ]