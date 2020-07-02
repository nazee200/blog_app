from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserListView
from . import views

urlpatterns = [
	path('', views.index,name="homepage"),
    path('home/', PostListView.as_view(),name="blog-home"),
     path('user/<str:username>', UserListView.as_view(),name="userview"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="detailview"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="deleteview"),
     path('post/<int:pk>/update/', PostUpdateView.as_view(),name="updateview"),
    path('post/new/', PostCreateView.as_view(),name="createview"),
    path('about/', views.detail,name="blog-about"),
    path('login/',views.login,name="blog-login"),
]
