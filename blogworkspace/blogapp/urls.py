from django.urls import path
from blogapp.views import *


urlpatterns = [
    
path('add-blog',addblog, name='addblog'),
path('blogs/<int:bg_id>/',viewBg, name="seeblog"),
path('my-blog',myblog,name="myblog"),
path('edit_blog/<int:bg_id>/',edit_blog,name="edit_blog"),
path('delete_blog/<int:bg_id>/',delete_blog,name="delete_blog"),
path("re/<int:blog_id>/",is_reccuring, name="re"),
path("profile",Userprofile,name="profile"),
path("editprofile",editpf,name="editprofile"),
path('blog/<int:blog_id>/comment/', add_comment, name='add_comment'),
path('blog/<int:blog_id>/like/', like_blog, name='like_blog'),


]