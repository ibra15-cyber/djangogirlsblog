from django.urls import path #urls 
from . import views  #views the code that will be rendered


urlpatterns = [
    path('', views.post_list),
    # path('post/<int:pk>/', views.post_detail, name='post.detail'), #post/1 post/2
   
]
