"""
URL configuration for blogweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from userapp.views import *
# from blogapp.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',register,name="register"),
    # path("home",home,name="home"),
    # path("login/",loginview,name="login"),
    # path("logout/",logoutview,name="logout"),
    # path('add-blog',addblog, name='addblog'),
    # path('blogs/<int:bg_id>/',viewBg, name="seeblog"),
    
    # path('my-blog',myblog,name="myblog"),
    # path('edit_blog/<int:bg_id>/',edit_blog,name="edit_blog"),
    # path('delete_blog/<int:bg_id>/',delete_blog,name="delete_blog"),
    
    # path("re/<int:blog_id>/",is_reccuring, name="re"),
    # path("profile",Userprofile,name="profile"),
    # path("editprofile",editpf,name="editprofile"),
    # path("helpspt",helSupport,name="helpspt"),
    # path("settings",Settings,name="settings"),
    path("",include("userapp.urls")),
    path("",include("blogapp.urls")),


    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
