from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/', views.create_comment, name='create_comment'),
    path('<int:board_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:board_pk>/comment/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('test/', views.test, name='test'),
]
