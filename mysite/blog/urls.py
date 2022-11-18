from django.urls import path #urls 
from . import views  #views the code that will be rendered


urlpatterns = [
    #goes to / show everything
    path('', views.post_list),
    #this link, post/1 goes to post_detail view with post detail html
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    #remember post is just our choosing
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
