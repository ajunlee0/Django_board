from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("new/", views.new_post, name="new_post"), # 새 글 작성
    path("post/<int:post_id>/", views.post_detail, name="post_detail"), # 글 보기
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"), # 댓글 작성
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),  # 공감
]
