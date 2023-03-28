from django.urls import path
from .views import RegisterApi, LoginApi, Logout

urlpatterns = [
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    path('logout/',Logout.as_view())
]
