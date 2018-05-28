from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path(r'comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('my_item', views.my_item, name='myitem'),
]
