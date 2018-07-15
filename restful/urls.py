from django.urls import path, include
from . import views
urlpatterns = [
    path('login', views.Login, name="Login"),
    path('account', views.Account, name="Account"),
    path('rank', views.GetRanking, name='GetRanking'),
]
