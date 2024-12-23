from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.BlogPostIndexView.as_view(), name='index'),
    path('create/', views.BlogPostCreateView.as_view(), name='create'),
    path('update/<slug:post_slug>/', views.BlogPostUpdateView.as_view(), name='update'),
    path('post/<slug:post_slug>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]
