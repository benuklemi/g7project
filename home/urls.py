from django.urls import path
from django.contrib.auth import views as auth_views

# from .forms import LoginForm
from .views import Login, Register, add_blogs, blogs, blog_comments, Profile


urlpatterns = [

    path("", blogs, name="blogs"),
    path("profile/", Profile, name="profile"),
    path("comments/", blog_comments, name="blog-comments"),
    path("login/", Login, name="login"),
    # path("logout", Login, name="login"),
    path("register/", Register, name="register"),
    path("add_blogs/", add_blogs, name="add-blogs"),
  
]
