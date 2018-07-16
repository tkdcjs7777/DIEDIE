from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.Login, name="Login"),
    path('account', views.Account, name="Account"),
    path('totalrank', views.GetTotalRank, name='GetTotalRank'),
    path('myrank/<user_id>', views.GetMyRank, name="GetMyRank"),
    
]
