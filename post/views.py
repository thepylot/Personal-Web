from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from .models import Post
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponse
import json

def home_view(request):
    #ALL 
    
    posts = Post.objects.all()[:6]
    posts_bg = Post.objects.all().order_by('-datetime')
    posts_first_three = Post.objects.all().order_by('-datetime')[:3]
    posts_middle_three = Post.objects.all().order_by('-datetime')[3:6]
    posts_end_three = Post.objects.all().order_by('-datetime')[6:9]
    
    #CATEGORIES
    category_game = Post.objects.all().filter(category="game")[:3]
    category_mobile = Post.objects.all().filter(category="mobile")[:3]
    category_software = Post.objects.all().filter(category="software")[:2] 
    category_space = Post.objects.all().filter(category="space")[:3] 
    category_science = Post.objects.all().filter(category="science")[:3] 
    category_social_media = Post.objects.all().filter(category="social media")[:3] 
    category_equipment = Post.objects.all().filter(category="equipment")[:3] 
  
    context = {
      
      'posts':posts,
      'posts_bg':posts_bg,
      'posts_first_three':posts_first_three,
      'posts_middle_three':posts_middle_three,
      'posts_end_three': posts_end_three,
      'category_game':category_game,
      'category_mobile':category_mobile,
      'category_software':category_software,
      'category_space':category_space,
      'category_science':category_science,
      'category_social_media':category_social_media,
      'category_equipment':category_equipment,


    }
    

    template="post/home.html"
    return render(request,template,context)

def lazy_load_posts(request):
  page = request.POST.get('page')
  posts = Post.objects.all()
  
  
  results_per_page = 5
  paginator = Paginator(posts, results_per_page)
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)
		
  # build a html posts list with the paginated posts
  posts_html = loader.render_to_string('test2.html', {'posts': posts})
  posts_html = posts_html.replace("\t", "")


  
  
  # package output data and return it as a JSON object
  output_data = {'posts_html':posts_html, 'has_next': posts.has_next()}

  
  return JsonResponse(output_data)
