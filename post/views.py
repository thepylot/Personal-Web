from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from .models import Post
from .forms import PostForm
from django.template import loader
from django.utils.text import slugify
from django.contrib import messages

def home_view(request):
    

    template="post/home.html"
    return render(request,template)


def blog(request):
    #ALL 
    
   
    posts = Post.objects.all().order_by('-published')
   
    
    #CATEGORIES
    category_game = Post.objects.all().filter(category="game")[:3]
    category_mobile = Post.objects.all().filter(category="mobile")[:3]
    category_software = Post.objects.all().filter(category="software")[:2] 
    category_space = Post.objects.all().filter(category="space")[:3] 
    category_science = Post.objects.all().filter(category="science")[:3] 
    category_social_media = Post.objects.all().filter(category="social media")[:3] 
    category_equipment = Post.objects.all().filter(category="equipment")[:3] 

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    if not page:
        page = paginator.num_pages
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
  
    context = {
      
      'posts':posts,
      'category_game':category_game,
      'category_mobile':category_mobile,
      'category_software':category_software,
      'category_space':category_space,
      'category_science':category_science,
      'category_social_media':category_social_media,
      'category_equipment':category_equipment,


    }

    template="post/blog.html"
    return render(request,template,context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    Post.objects.filter(id=post.id).update(views=F('views') + 1)
   
    
   


    context = {
        'post':post,   
        }
    return render (request, 'post/detail.html', context )


def admin(request):
    template="dashboard/admin.html"
    return render(request, template) 


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
  
    posts = Post.objects.all().order_by('-published')
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Form submission successful')
  
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    if not page:
        page = paginator.num_pages
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
        
    context={
        'form':form,
        'posts':posts,
    }
    return render (request, 'dashboard/post_create.html',context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        return redirect ('dashboard:create')
      
    context = {
        'form':form,
        'post':post,
      }
    return render (request, 'dashboard/post_update.html', context )


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect ('dashboard:create')

