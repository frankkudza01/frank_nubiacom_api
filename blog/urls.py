from django.urls import path
from blog import views

urlpatterns=[
    path('blog/', views.PostList.as_view()),
    path('blog/create/',views.PostCreate.as_view()),
    path('blog/<int:pk>',views.PostDetail.as_view()),
    path('blog/<int:pk>/edit/',views.PostEdit.as_view()),

    
]
