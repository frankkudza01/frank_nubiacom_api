from django.urls import path
from blog import views

urlpatterns=[
    path('blog/', views.post_list),
    path('blog/post/<int:pk>',views.post_detail)
]
