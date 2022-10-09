from django.urls import path
from blog import views

urlpatterns = [
    path('<int:user_id>/posts/', views.PostListView.as_view(), name='posts_list'),
    path('<int:user_id>/posts/<uuid:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:user_id>/posts/<uuid:post_id>/comments/', views.CommentListView.as_view(), name='comments_list'),
    path('<int:user_id>/posts/<uuid:post_id>/comments/<uuid:pk>', views.CommentDetailView.as_view(), name='comment_detail')
]
