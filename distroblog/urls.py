from . import views
from django.urls import path

urlpatterns = [
    path('detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('comment/<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('comment/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('like-post', views.like_post, name='like_post'),
]