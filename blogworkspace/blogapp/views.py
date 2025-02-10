from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required   #its basic use is that to login to auth
# Create your views here.
@login_required    #its means we need to login to access this view
def addblog(request):
    if request.method == 'POST':
       title=request.POST.get("title")  
       description=request.POST.get("description")  
       blog_image=request.FILES["blog_image"]     # for image upload  we want to use .FILES not requeried POST
       
       blog=Blog()      # its a object
       blog.title=title
       blog.description=description
       blog.blog_image=blog_image
       blog.user=request.user
       blog.save()      #save method to save the data in database which is in models.py and made up by me
       return redirect('home')
       
    else:
        return render(request,"addblog.html")    
        
        
@login_required
def viewBg(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)
    print(f'foundedblog{blog}')
    return render(request, "vb.html",{"blog": blog})

#-----------------------------------------------------------------------------------
@login_required
def myblog(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, "myblog.html", {"blogs": blogs})



    
    
@login_required
def delete_blog(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)
    blog.delete()
    return redirect('myblog')

@login_required
def edit_blog(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)

    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        blog_image = request.FILES.get("blog_image")  # Use .get() to avoid error

        blog.title = title
        blog.description = description
        
        if blog_image:
            blog.blog_image = blog_image  #blog img

        blog.save()
        return redirect('myblog')

    return render(request, "editblog.html", {"blog": blog})
    
#-------------------------------------------------------------------------
@login_required
def searchbg(request):
    q=request.GET.get("q")
    blogs= Blog.objects.filter(description__contains=q)  
    return render(request, "home.html",{"blogs": blogs})


    
def is_reccuring(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request,"is_recc.html",{'blog':blog})


def Userprofile(request):
    blogs=Blog.objects.filter(user=request.user).order_by("create_at")
    
    return render(request, 'profile.html',{"blogs":blogs})


# COMMENT FROM NEW_FEATURE BRANCH
from django.views import View

class SaveBlogsOnPorfileView(View):
    pass 

# --03e0edededwe933933237777733332233e